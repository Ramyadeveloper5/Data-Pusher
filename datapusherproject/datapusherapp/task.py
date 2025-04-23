from celery import shared_task
import requests
from django.utils import timezone
from .models import LogModel, DestinationModel, AccountModel
import logging

logger = logging.getLogger(__name__)


@shared_task
def data_send_to_destination(account_id, event_id, data):
    
    try:
        account = AccountModel.objects.get(id = account_id)
    except AccountModel.DoesNotExist:
       return f"Account with ID {account_id} does not exist."
    
    destinations = DestinationModel.objects.filter(account = account)
    
    for destination in destinations:
        headers = destination.headers
        url = destination.destination_url
        method = destination.http_method.upper()
        status = 'Failed'  # Default status
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, params=data )
            else:
                response = requests.request(method, url, json=data, headers=headers )
            
            status = 'Success' if response.status_code in [200, 201] else 'Failed'
        
        except Exception as e:
            status = 'Failed'
            logger.error(f"Failed to send data to {url}: {e}")
        
        # Log Creation
        LogModel.objects.create(
            event_id = event_id,
            account = account,
            received_timestamp=timezone.now(),
            processed_timestamp=timezone.now(),
            destination=destination,
            received_data=data,
            status=status
        )
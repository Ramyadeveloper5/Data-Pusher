from rest_framework import viewsets, permissions
from .serializers import LogModelSerializer, AccountModelSerializer, DestinationModelSerializer
from .models import AccountModel, DestinationModel, LogModel
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from django.utils import timezone
from django.http import JsonResponse
import uuid, json
from rest_framework.throttling import UserRateThrottle
from .task import data_send_to_destination
from django_filters import rest_framework as filters
from .filters import DestinationFilter, LogFilter


# Account
class AccountViewSet(viewsets.ModelViewSet):
    queryset = AccountModel.objects.all()
    serializer_class = AccountModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# Destination
class DestinationViewSet(viewsets.ModelViewSet):
    queryset = DestinationModel.objects.all()
    serializer_class = DestinationModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend)
    filterset_class = DestinationFilter
    
# Log
class LogViewSet(viewsets.ModelViewSet):
    queryset = LogModel.objects.all()
    serializer_class = LogModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LogFilter
    
    
# Data Handler Using API

class FivePerSecond(UserRateThrottle):
    rate = '5/second'
    
@api_view(['POST'])
@throttle_classes([FivePerSecond])
def incoming_data(request):
    token = request.headers.get('CL-X-TOKEN')
    event_id = request.headers.get('CL-X-EVENT-ID')
    
    if not token:
        return JsonResponse({'success' : False, 'message' : 'UnAuthenticated'}, status = 401)
    
    try:
        account = AccountModel.objects.get(app_secret_token = token)
    except AccountModel.DoesNotExist:
        return JsonResponse({"success": False, "message": "Unauthenticated"}, status=401)
    
    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"success": False, "message": "Invalid Data"}, status=400)
    
    data_send_to_destination.delay(account.account_id, event_id, data)
    return JsonResponse({"success": True, "message": "Data Received"})
    





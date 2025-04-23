from django_filters import rest_framework as filters
from .models import DestinationModel, LogModel

# API to Get Destinations Available for the Account (by Account ID)

class DestinationFilter(filters.FilterSet):
    account_id = filters.NumberFilter(field_name="account__id", lookup_expr='exact')

    class Meta:
        model = DestinationModel
        fields = ['account_id']
        
        
# API to Get All Logs with Filters (Destination ID, Status, Timestamps)

class LogFilter(filters.FilterSet):
    destination_id = filters.NumberFilter(field_name="destination__id", lookup_expr='exact')
    status = filters.CharFilter(field_name="status", lookup_expr='exact')
    received_timestamp = filters.DateTimeFilter(field_name="received_timestamp", lookup_expr='gte')
    processed_timestamp = filters.DateTimeFilter(field_name="processed_timestamp", lookup_expr='gte')

    class Meta:
        model = LogModel
        fields = ['destination_id', 'status', 'received_timestamp', 'processed_timestamp']

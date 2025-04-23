from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

# Role Model
class RoleModel(models.Model):
    role_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    role_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Role Name is {self.role_name}"
    
# Account Model
class AccountModel(models.Model):
    account_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    account_name = models.CharField(max_length=100, unique=True)
    app_secret_token = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='accounts_created', on_delete=models.CASCADE)
    updated_by = models.ForeignKey('auth.User', related_name='accounts_updated', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Account Name is : {self.account_name}"
    
# Destination Model
class DestinationModel(models.Model):
    account = models.ForeignKey(AccountModel, related_name='destinations', on_delete=models.CASCADE)
    destination_url = models.URLField()
    http_method = models.CharField(max_length=10)
    headers = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='destinations_created', on_delete=models.CASCADE)
    updated_by = models.ForeignKey('auth.User', related_name='destinations_updated', on_delete=models.CASCADE)
    
# Account Member Model
class AccountMemberModel(models.Model):
    account = models.ForeignKey(AccountModel, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    role = models.ForeignKey(RoleModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='accountmembers_created', on_delete=models.CASCADE)
    updated_by = models.ForeignKey('auth.User', related_name='accountmembers_updated', on_delete=models.CASCADE)
    
# Log Model
class LogModel(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    account = models.ForeignKey(AccountModel, on_delete=models.CASCADE)
    received_timestamp = models.DateTimeField()
    processed_timestamp = models.DateTimeField()
    destination = models.ForeignKey(DestinationModel, on_delete=models.CASCADE)
    received_data = models.JSONField()
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Received Data is {self.received_data}"
    
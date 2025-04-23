from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import AccountModel, DestinationModel, AccountMemberModel, LogModel

@receiver(post_delete, sender=AccountModel)
def cascade_delete_related(sender, instance, **kwargs):
    DestinationModel.objects.filter(account=instance).delete()
    AccountMemberModel.objects.filter(account=instance).delete()
    LogModel.objects.filter(account=instance).delete()

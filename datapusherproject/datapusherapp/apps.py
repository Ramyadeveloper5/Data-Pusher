from django.apps import AppConfig


class DatapusherappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'datapusherapp'

def ready(self):
    import datapusherapp.signals

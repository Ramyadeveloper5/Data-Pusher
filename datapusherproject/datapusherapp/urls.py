from django.urls import path
from datapusherapp.auth.views import RegisterView, LoginView, LogoutView
from .views import DestinationViewSet, LogViewSet, incoming_data

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('destinations/', DestinationViewSet.as_view({'get': 'list'}), name='destination-list'),
    path('logs/', LogViewSet.as_view({'get': 'list'}), name='log-list'),
    path('server/incoming_data/', incoming_data, name='incoming-data')
    ]
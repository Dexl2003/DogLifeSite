from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home/'),
    path('services/', services, name='services/'),
    path('contacts/', contacts, name='contacts/'),
    path('about/', about, name='about/'),
    path('auth/', auth, name='auth/'),
    path('auth/<slug:auth_id>', auth_id, name='auth_id'),
    path('register/<slug:reg_id>', register, name='register'),
    path('record/<slug:record_id>', record, name='record'),
    path('account', account, name='account/'),
]
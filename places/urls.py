from django.urls import path
from .views import places

urlpatterns = [
    path('', places, name='places-list')
]
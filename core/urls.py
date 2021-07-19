from django.urls import path
from .views import homepage, profile

urlpatterns = [
    path('', homepage, name='homepage'),
    path('profile/', profile, name='profile')
]
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import change_password
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include

urlpatterns = [
    url('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

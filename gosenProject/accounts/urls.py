from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import change_password
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('change-password/', change_password),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
        name='password_reset'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm')
]

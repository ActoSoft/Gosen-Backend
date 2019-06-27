from celery import task
from django.template.loader import get_template, render_to_string
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.conf import settings

def send_email(context, reset_password_token):
    message = get_template('email/user_reset_password.html').render(context)
    email = EmailMessage("Recuperación de contraseña para {title}".format(title="Gosen"), message, from_email='actosoftcommunity@gmail.com', to=[reset_password_token.user.email])
    email.content_subtype = "html"
    email.send()
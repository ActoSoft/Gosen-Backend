from celery import task
from django.template.loader import get_template, render_to_string
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.conf import settings


@task
def send_email(context):
    message = get_template('email/user_reset_password.html').render(context)
    email = EmailMessage("Recuperación de contraseña para {title}".format(title="Gosen"), message, from_email='actosoftcommunity@gmail.com', to=[context['email']])
    email.content_subtype = "html"
    email.send()

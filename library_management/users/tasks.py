from celery import shared_task
from django.core.mail import send_mail
from .models import CustomUser


@shared_task
def send_welcome_email(user_id):
    user = CustomUser.objects.get(id=user_id)
    subject = 'Welcome to our application'
    message = f'Thank you for registering, {user.user_name}! Welcome!'
    from_email = 'noreply@rsl.ru'
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
    return None

import logging
from celery import shared_task
from authapp.models import User
from django.core.mail import send_mail


@shared_task
def send_feedback_to_email(message_body: str, message_from: int = None) -> None:
    if message_from is not None:
        user_from = User.objects.filter(pk=message_from).first().get_full_name()
    else:
        user_from = 'Anonim'

    send_mail(
        subject=f'fFeedback from: {user_from}',
        message=message_body,
        recipient_list=['support@blms.local'],
        from_email='support@blms.local',
        fail_silently=False
    )


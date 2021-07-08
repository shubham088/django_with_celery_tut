from celery import shared_task
import time
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    time.sleep(duration)
    return None


@shared_task
def send_mail_using_celery():
    send_mail(
        'with celery',
        'this mail is with celery.',
        'shubhamsharma0296@gmail.com',
        ['shubhamsharma0296@gmail.com'],
        fail_silently=False,
    )
    return None
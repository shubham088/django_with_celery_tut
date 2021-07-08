from django.shortcuts import render
from django.http import HttpResponse
from core.tasks import sleepy, send_mail_using_celery
from django.core.mail import send_mail

# Create your views here.

def index(request):
    # sleepy(15) # without use of celery
    sleepy.delay(15) # this is with celery
    return HttpResponse('<b>Hello</b>')



def send_mail_to_user(request):
    send_mail(
        'without celery',
        'this mail is without celery.',
        'shubhamsharma0296@gmail.com',
        ['shubhamsharma0296@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse('<b>Email Sent</b>')

def send_mail_to_user_with_celery(request):
    send_mail_using_celery.delay()
    return HttpResponse('<b>Email Sent with celery</b>')


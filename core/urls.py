from django.urls import path, include
from core.views import index, send_mail_to_user, send_mail_to_user_with_celery

urlpatterns = [
    path('', index, name='index'),
    path('send_mail_no_celery/', send_mail_to_user, name='send_mail'),
    path('send_mail_with_celery/', send_mail_to_user_with_celery, name='send_mail')
]
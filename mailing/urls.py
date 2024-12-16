from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import base

app_name = MailingConfig.name

urlpatterns = [
    path("", base, name="base"),
]

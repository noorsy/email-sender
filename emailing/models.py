import pickle
import base64

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

# from oauth2client.django_orm import FlowField
from oauth2client.contrib.django_util.models import CredentialsField
from oauth2client.contrib.django_util.storage import DjangoORMStorage


class CredentialsModel(models.Model):
  id = models.ForeignKey(User, primary_key=True)
  credential = CredentialsField()


class CredentialsAdmin(admin.ModelAdmin):
    pass


admin.site.register(CredentialsModel, CredentialsAdmin)

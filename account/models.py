from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUserModel(AbstractUser):
    contact = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)



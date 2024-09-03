from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]

    address = models.CharField(blank=True, null=True, max_length=255)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, blank=True, null=True, max_length=1)
    phone = models.CharField(blank=True, null=True, max_length=15)
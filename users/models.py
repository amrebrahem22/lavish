from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]

CURRENCY = [
    ('usd', "USD"),
    ('egp', 'EGP')
]

LANGUAGE = [
    ("en", 'EN'),
    ('ar', 'AR')
]


class User(AbstractUser):
    gender = models.CharField(choices=GENDER, max_length=10)
    avatar = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE, null=True, blank=True, max_length=2)
    currency = models.CharField(
        choices=CURRENCY, null=True, blank=True, max_length=3)
    superhost = models.BooleanField(default=False)

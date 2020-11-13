import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.shortcuts import reverse
from django.template.loader import render_to_string

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
        choices=LANGUAGE, null=True, blank=True, max_length=2, default=LANGUAGE[0])
    currency = models.CharField(
        choices=CURRENCY, null=True, blank=True, max_length=3, default=CURRENCY[0])
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
        
    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "Verify Lavish Account",
                strip_tags(html_message),
                settings.DEFAULT_FROM_EMAIL,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return
    
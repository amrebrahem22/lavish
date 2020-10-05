from django.conf import settings
from django.db import models
from core.models import AbstractTimestamp


class Conversation(AbstractTimestamp):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return str(self.created)


class Messaage(AbstractTimestamp):
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.text}"

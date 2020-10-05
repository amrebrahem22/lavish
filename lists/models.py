from django.conf import settings
from django.db import models
from rooms.models import Room
from core.models import AbstractTimestamp


class List(AbstractTimestamp):
    name = models.CharField(max_length=80)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Room)

    def __str__(self):
        return self.name

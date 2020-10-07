from django.conf import settings
from django.db import models
from rooms.models import Room
from core.models import AbstractTimestamp


class List(AbstractTimestamp):
    name = models.CharField(max_length=80)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='lists')
    rooms = models.ManyToManyField(Room, related_name='lists')

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "Number of Rooms"

from django.conf import settings
from django.db import models
from django.utils import timezone
from rooms.models import Room
from core.models import AbstractTimestamp


STATUS = [
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('canceled', 'Canceled'),
]

class Reservation(AbstractTimestamp):
    status = models.CharField(choices=STATUS, max_length=12, default=STATUS[0])
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True
    
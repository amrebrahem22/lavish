from django.conf import settings
from django.db import models
from rooms.models import Room

STATUS = [
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('canceled', 'Canceled'),
]

class Reservation(models.Model):
    status = models.CharField(choices=STATUS, max_length=12, default=STATUS[0])
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"

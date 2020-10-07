from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room', 'status', 'guest', 'in_progress', 'is_finished')

admin.site.register(Reservation, ReservationAdmin)

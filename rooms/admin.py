from django.contrib import admin
from .models import Room, RoomType, Amenity, Facility, HouseRule, Photo


admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Amenity)
admin.site.register(Facility)
admin.site.register(HouseRule)
admin.site.register(Photo)

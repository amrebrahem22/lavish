from django.contrib import admin
from .models import Room, RoomType, Amenity, Facility, HouseRule, Photo


class RoomAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Basic Info', {
            "fields": ('name', 'description', 'country', 'address', 'city', 'price')
        }),
        ('Times', {
            "fields": ('check_in', 'check_out', 'instant_book')
        }),
        ('Spaces', {
            "fields": ('guestes', 'beds', 'bedrooms', 'baths',)
        }),
        ('More about the Spaces', {
            "fields": ('amenities', 'facilities', 'house_rule',)
        }),
        ('Last Detail', {
            "fields": ('host',)
        }),
    ]

    list_display = [
        'name',
        'country',
        'city',
        'price',
        'address',
        'beds',
        'bedrooms',
        'baths',
        'check_in',
        'check_out',
        'instant_book',
        'count_ameneties',
    ]

    list_filter = ['name', 'city', 'price', 'country']
    filter_horizontal = ('amenities', 'facilities', 'house_rule',)

    def count_ameneties(self, obj):
        return obj.ameneties.count()


admin.site.register(Room, RoomAdmin)
admin.site.register(RoomType)
admin.site.register(Amenity)
admin.site.register(Facility)
admin.site.register(HouseRule)
admin.site.register(Photo)

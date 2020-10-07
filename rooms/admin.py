from django.contrib import admin
from django.utils.html import mark_safe
from .models import Room, RoomType, Amenity, Facility, HouseRule, Photo


class PhotoInline(admin.TabularInline):
    model = Photo

class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    fieldsets = [
        ('Basic Info', {
            "fields": ('name', 'description', 'country', 'address', 'city', 'price', 'room_type')
        }),
        ('Times', {
            "fields": ('check_in', 'check_out', 'instant_book')
        }),
        ('Spaces', {
            "fields": ('guests', 'beds', 'bedrooms', 'baths',)
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
        'count_amenities',
        'total_reviews',
        'count_photos',
    ]

    list_filter = ['name', 'city', 'price', 'country']
    filter_horizontal = ('amenities', 'facilities', 'house_rule',)
    search_fields = ('city', 'host__username')
    raw_id_fields = ('host',)

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "Amenity Count"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


class RoomActions(admin.ModelAdmin):
    list_display = ('name', 'used_by')

    def used_by(self, obj):
        return obj.rooms.count()


class RoomPhotoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_thumbnail')

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width='50px' src='{obj.file.url}' />")

    get_thumbnail.short_description = "Thumbnail"


admin.site.register(Room, RoomAdmin)
admin.site.register(RoomType, RoomActions)
admin.site.register(Amenity, RoomActions)
admin.site.register(Facility, RoomActions)
admin.site.register(HouseRule, RoomActions)
admin.site.register(Photo, RoomPhotoAdmin)

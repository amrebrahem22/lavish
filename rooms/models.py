from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from core.models import AbstractTimestamp

User = settings.AUTH_USER_MODEL


class AbstarctItemModel(models.Model):
    name = models.CharField(max_length=140)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstarctItemModel):
    pass

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstarctItemModel):
    pass

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstarctItemModel):
    pass

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstarctItemModel):
    pass

    class Meta:
        verbose_name = "House Rule"


class Photo(AbstarctItemModel):
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='photos')


class Room(AbstractTimestamp):
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guestes = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rooms")
    room_type = models.ForeignKey(
        RoomType, null=True, on_delete=models.SET_NULL, related_name="rooms")
    amenities = models.ManyToManyField(Amenity, blank=True, related_name="rooms")
    facilities = models.ManyToManyField(Facility, blank=True, related_name="rooms")
    house_rule = models.ManyToManyField(HouseRule, blank=True, related_name="rooms")

    def __str__(self):
        return self.name

    def total_reviews(self):
        all_reviews = self.reviews.all()
        all_rating = 0
        for review in all_reviews:
            all_rating += review.rating_average()
        return all_rating / len(all_reviews)
        
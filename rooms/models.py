from django.db import models
from django.urls import reverse
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
    room = models.ForeignKey(
        'Room', on_delete=models.CASCADE, related_name='photos')


class Room(AbstractTimestamp):
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="rooms")
    room_type = models.ForeignKey(
        RoomType, null=True, on_delete=models.SET_NULL, related_name="rooms")
    amenities = models.ManyToManyField(
        Amenity, blank=True, related_name="rooms")
    facilities = models.ManyToManyField(
        Facility, blank=True, related_name="rooms")
    house_rules = models.ManyToManyField(
        HouseRule, blank=True, related_name="rooms")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})
    
    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0
    
    def first_photo(self):
        try:
            photo, = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos

    def get_beds(self):
        if self.beds == 1:
            return "1 bed"
        else:
            return f"{self.beds} beds"

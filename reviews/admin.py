from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'rating_average')

admin.site.register(Review, ReviewAdmin)

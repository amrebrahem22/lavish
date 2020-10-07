from django.contrib import admin
from .models import List

class ListsAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'count_rooms')
    search_fields = ('name',)
    filter_horizontal = ('rooms',)

admin.site.register(List, ListsAdmin)

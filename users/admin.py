from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Profile', {
            "fields": ('avatar', 'gender', 'bio', 'birthdate', 'language', 'currency', 'superhost'),
        }),
    )

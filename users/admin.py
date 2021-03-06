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

    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'language',
        'currency',
        'superhost',
        'is_staff',
        'is_superuser',
        "email_verified",
        "email_secret",
    )

    list_filter = UserAdmin.list_filter + ('superhost', )

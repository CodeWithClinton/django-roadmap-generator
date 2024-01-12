from django.contrib import admin
from .models import CustomUser, Profile
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'passed', 'project')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
    

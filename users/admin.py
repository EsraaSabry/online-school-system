from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import Group

# Register your models here.

from .models import User

class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'us_studen', 'is_teacher', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'us_studen', 'is_teacher', 'password')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    list_display = ['email', 'username', 'us_studen', 'is_teacher']
    search_fields = ('email', 'username')
    ordering = ('email',)




admin.site.register(User,UserAdmin)
admin.site.unregister(Group)


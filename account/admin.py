from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    list_display = ('id', 'email', 'name', 'tc', 'is_active', 'is_admin')
    list_display_links = ('email',)
    list_filter = ('is_admin', 'is_active')
    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = []

    # 🔒 Password readonly (hashed dikhega)
    readonly_fields = ('password',)

    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal Information', {'fields': ('name', 'tc')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'tc', 'password1', 'password2'),
        }),
    )
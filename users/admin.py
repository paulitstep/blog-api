from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import NewUser

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name',)
    list_filter = ('email', 'user_name', 'is_staff', 'is_active')
    list_display = ('email', 'user_name', 'is_staff', 'is_active')
    ordering = ('-start_date',)

    fieldsets = (
        (None, {'fields': ('email', 'user_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Personal', {'fields': ('about',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2', 'is_staff', 'is_active'), }),
    )




admin.site.register(NewUser, UserAdminConfig)

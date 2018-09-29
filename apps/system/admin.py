from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class UserProfileAdmin(UserAdmin):

    list_display = ['id', 'name', 'username', 'mobile', 'email', 'gender']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('用户信息', {'fields': ('name', 'birthday', 'gender', 'image')}),
        ('联系信息', {'fields': ('mobile', 'email')}),
        ('用户权限', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('岗位信息', {'fields': ('department', 'post', 'superior', 'roles')})
    )


admin.site.register(User, UserProfileAdmin)
admin.site.register(models.Structure)


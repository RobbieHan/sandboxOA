from django.contrib import admin

from django.contrib.auth import get_user_model


User = get_user_model()

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'mobile', 'email']


admin.site.register(User, UserProfileAdmin)

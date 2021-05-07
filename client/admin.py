from django.contrib import admin
from client.models import User
from django.utils.html import format_html

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'photo',
        'username'
    ]

    list_display_links = [
        'username'
    ]

    class Meta:
        model = User

admin.site.register(User, UserAdmin)

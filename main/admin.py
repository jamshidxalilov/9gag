from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name_uz',
        'name_ru'
    ]

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'file'
    ]

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
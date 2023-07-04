from django.contrib import admin

from .models import Image, ResizedImage


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(ResizedImage)
class ResizedImageAdmin(admin.ModelAdmin):
    pass

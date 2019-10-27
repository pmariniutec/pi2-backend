from django.contrib import admin

from .models import Sighting, SightingImage


class ImageInline(admin.TabularInline):
    model = SightingImage
    fields = ['url']


@admin.register(Sighting)
class SightingAdmin(admin.ModelAdmin):
    list_display = ['user']
    fields = ['user']
    inlines = [ImageInline]

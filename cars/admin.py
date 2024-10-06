from django.contrib import admin
from django.utils.html import format_html

from .models import CarBrand, Car


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):

    list_display = ('car_brand_name', 'is_featured')
    list_display_links = ('car_brand_name', )

    prepopulated_fields = {'slug': ('car_brand_name', )}
    search_fields = ('car_brand_name', )
    ordering = ('-updated_at', 'is_featured')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, obj):
        return format_html(f'<img src="{obj.car_title_photo.url}" width="50"/>')
    thumbnail.short_description = 'Photo'

    list_display = ('thumbnail', 'car_title', 'mileage', 'year', 'price', 'in_stock')
    list_display_links = ('thumbnail', 'car_title',)
    prepopulated_fields = {'slug': ('car_title', 'fuel_type', 'transmission', 'color')}
    list_filter = ('car_title', 'fuel_type', 'transmission', 'color', 'in_stock')

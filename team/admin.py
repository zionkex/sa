from django.contrib import admin

from .models import Team


@admin.register(Team)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name',]


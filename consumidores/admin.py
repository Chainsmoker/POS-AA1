from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Consumidores

@admin.register(Consumidores)
class CustomAdminClass(ModelAdmin):
    pass
from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Descuentos

@admin.register(Descuentos)
class CustomAdminClass(ModelAdmin):
    pass
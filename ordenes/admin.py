from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Orden

@admin.register(Orden)
class CustomAdminClass(ModelAdmin):
    list_display = ('consumidor', 'total', 'fecha', 'estado', 'descuento',)
    list_filter = ('consumidor', 'fecha', 'estado', 'descuento',)
    search_fields = ('consumidor', 'fecha', 'estado', 'descuento',)
    ordering = ('-created_at',)
    readonly_fields = ('total',)
    fieldsets = (
        ('Información de la orden', {
            'fields': ('consumidor', 'productos', 'total', 'fecha', 'estado', 'descuento')
        }),
    )
    filter_horizontal = ('productos',)
    date_hierarchy = 'fecha'
    save_on_top = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    save_on_bottom = True
    save_and_add_another = True

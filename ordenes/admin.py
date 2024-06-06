from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Orden, OrdenProducto

@admin.register(Orden)
class CustomAdminClass(ModelAdmin):
    list_display = ('order_number', 'consumidor', 'total', 'estado', 'descuento', 'pagado')
    list_filter = ('consumidor', 'estado', 'descuento',)
    search_fields = ('consumidor', 'estado', 'descuento',)
    ordering = ('-created_at',)
    fieldsets = (
        ('Información de la orden', {
            'fields': ('consumidor', 'orden_producto', 'total', 'estado', 'descuento', 'pagado')
        }),
    )
    filter_horizontal = ('orden_producto',)
    save_on_top = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    save_on_bottom = True
    save_and_add_another = True

@admin.register(OrdenProducto)
class CustomAdminClass(ModelAdmin):
    list_display = ('producto', 'cantidad', 'sub_total',)
    list_filter = ('producto', 'cantidad', 'sub_total',)
    search_fields = ('producto', 'cantidad', 'sub_total',)
    ordering = ('-created_at',)
    readonly_fields = ('sub_total',)
    fieldsets = (
        ('Información del producto', {
            'fields': ('producto', 'cantidad', 'sub_total')
        }),
    )
    save_on_top = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    save_on_bottom = True
    save_and_add_another = True
from django.contrib import admin
from unfold.admin import ModelAdmin
from django.utils.html import format_html
from .models import Productos

@admin.register(Productos)
class CustomAdminClass(ModelAdmin):
    def producto_imagen(self, obj):
        url = obj.imagen.url
        return format_html(f'<img src="{url}" width="70" height="70">')
    
    list_display = ('producto_imagen', 'nombre', 'precio', 'stock', 'categoria', 'creado',)
    list_filter = ('stock', 'creado', 'actualizado')
    search_fields = ('nombre', 'precio', 'categoria', 'stock')
    ordering = ('-creado',)
    readonly_fields = ('creado', 'actualizado',)
    fieldsets = (
        ('Información del producto', {
            'fields': ('nombre', 'precio', 'stock', 'categoria', 'descripcion')
        }),
        ('Información extra', {
            'fields': ('imagen', 'creado', 'actualizado')
        }),
    )
    date_hierarchy = 'creado'
    save_as = True

admin.site.site_header = 'E-commerce Administrador'                    
admin.site.index_title = 'Admin area'                
admin.site.site_title = 'E-commerce Admin' 
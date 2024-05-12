from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Categorias

@admin.register(Categorias)
class CustomAdminClass(ModelAdmin):
    list_display = ('nombre', 'descripcion',)
    list_filter = ('creado', 'actualizado')
    search_fields = ('nombre', 'descripcion')
    ordering = ('-creado',)
    readonly_fields = ('creado', 'actualizado',)
    fieldsets = (
        ('Información de la categoria', {
            'fields': ('nombre', 'descripcion')
        }),
        ('Información extra', {
            'fields': ('creado', 'actualizado')
        }),
    )
    date_hierarchy = 'creado'
    save_as = True
    
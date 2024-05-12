from django.db import models

class Descuentos(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Descuento'
        verbose_name_plural = 'Descuentos'
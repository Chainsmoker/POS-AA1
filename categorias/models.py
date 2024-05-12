from django.db import models

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
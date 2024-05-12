from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey('categorias.Categorias', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    #categoria = models.ForeignKey('categorias.Categorias', on_delete=models.CASCADE)

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    def imagen_tag(self):
        if self.imagen:
            return u'<img src="%s" />' % self.imagen.url
        else:
            return 'No hay imagen'

    imagen_tag.short_description = 'Imagen'
    imagen_tag.allow_tags = True

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
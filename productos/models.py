from django.db import models

class Productos(models.Model):
    TALLAS = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'),
        ('XXXL', 'Extra Extra Extra Large'),
    )
    
    sku = models.CharField(max_length=100, unique=True, null=True)
    nombre = models.CharField(max_length=100)
    mini_descripcion = models.TextField()
    categoria = models.ForeignKey('categorias.Categorias', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagenes = models.ManyToManyField('ProductosImagenes', blank=True)
    mas_vendido = models.BooleanField(default=False)
    mejor_valorado = models.BooleanField(default=False)
    #categoria = models.ForeignKey('categorias.Categorias', on_delete=models.CASCADE)
    
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    dimensiones = models.CharField(max_length=100)
    tallas = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=100, unique=True)

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

    def save(self, *args, **kwargs):
        self.slug = self.nombre.lower().replace(' ', '-')
        super(Productos, self).save(*args, **kwargs)

    def get_tallas(self):
        return self.tallas.split(',')

class ProductosImagenes(models.Model):
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'

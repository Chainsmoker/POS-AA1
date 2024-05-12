from django.db import models

CHOICES_ESTADO = (
    ('pendiente', 'Pendiente'),
    ('en camino', 'En camino'),
    ('entregado', 'Entregado'),
)

class Orden(models.Model):
    consumidor = models.ForeignKey('consumidores.Consumidores', on_delete=models.CASCADE)
    productos = models.ManyToManyField('productos.Productos')
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateField()
    estado = models.CharField(max_length=20, choices=CHOICES_ESTADO, default='pendiente')
    descuento = models.ForeignKey('descuentos.Descuentos', on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.estado
    
    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
    
    def get_total(self):
        return sum([producto.precio for producto in self.productos.all()])
    
    def get_descuento(self):
        if self.descuento:
            return self.total * (self.descuento.porcentaje / 100)
        return 0

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.total = self.get_total()
        self.total -= self.get_descuento()
        super().save(*args, **kwargs) 
from django.db import models
from decimal import Decimal
import uuid 

def generate_order_id():
    return str(uuid.uuid4())

def generate_order_number():
    import random
    return random.randint(100000, 999999)

CHOICES_ESTADO = (
    ('pendiente', 'Pendiente'),
    ('en camino', 'En camino'),
    ('entregado', 'Entregado'),
)

class Orden(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_order_id, editable=False)
    order_number = models.CharField(max_length=32, null=False, editable=False, default=generate_order_number, unique=True)
    consumidor = models.ForeignKey('consumidores.Consumidores', on_delete=models.CASCADE)
    orden_producto = models.ManyToManyField('ordenes.OrdenProducto')
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=CHOICES_ESTADO, default='pendiente')
    pagado = models.BooleanField(default=False)
    descuento = models.ForeignKey('descuentos.Descuentos', on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.estado
    
    def save(self, *args, **kwargs):
        total = 0
        for item in self.orden_producto.all():
            total += item.sub_total
        
        self.total = total
        super().save(*args, **kwargs)

    def get_total_tax(self):
        return self.total + 19
    
    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
    
class OrdenProducto(models.Model):
    producto = models.ForeignKey('productos.Productos', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    sub_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.producto.nombre

    class Meta:
        verbose_name = 'Orden Producto'
        verbose_name_plural = 'Ordenes Productos'

    def save(self, *args, **kwargs):
        self.sub_total = Decimal(self.producto.precio) * Decimal(self.cantidad)
        super().save(*args, **kwargs)
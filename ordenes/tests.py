from django.test import TestCase
from productos.models import Productos
from consumidores.models import Consumidores
from descuentos.models import Descuentos

from .models import Orden

class OrdenTestCase(TestCase):
    def setUp(self):
        self.consumidor = Consumidores(
            nombre='Consumidor de prueba',
            email='consumidor@gmail.com'
        )
        self.consumidor.save()

        self.producto1 = Productos(
            nombre='Producto 1',
            descripcion='Este es un producto de prueba',
            precio=19.99,
            stock=10,
            imagen=None
        )
        self.producto1.save()

        self.producto2 = Productos(
            nombre='Producto 2',
            descripcion='Este es otro producto de prueba',
            precio=9.99,
            stock=20,
            imagen=None
        )
        self.producto2.save()

        self.descuento = Descuentos(
            titulo='Descuento de prueba',
            porcentaje=10
        )
        self.descuento.save()

        self.orden = Orden(
            consumidor=self.consumidor,
            estado='Pendiente',
            fecha='2022-01-01',
            descuento=self.descuento
        )
        self.orden.save()
        self.orden.productos.add(self.producto1)
        self.orden.productos.add(self.producto2)

    def test_consumidor_orden(self):
        self.assertEqual(self.orden.consumidor, self.consumidor)

    def test_productos_orden(self):
        self.assertEqual(self.orden.productos.count(), 2)
        self.assertIn(self.producto1, self.orden.productos.all())
        self.assertIn(self.producto2, self.orden.productos.all())

    def test_total_orden(self):
        self.assertEqual(self.orden.total, 29.98)

    def test_fecha_orden(self):
        self.assertEqual(self.orden.fecha, '2024-07-01')

    def test_estado_orden(self):
        self.assertEqual(self.orden.estado, 'Pendiente')

    def test_descuento_orden(self):
        self.assertEqual(self.orden.descuento, self.descuento)

    def test_get_total(self):
        self.assertEqual(self.orden.get_total(), 29.98)

    def test_get_descuento(self):
        self.assertEqual(self.orden.get_descuento(), 2.99)

    def test_str_orden(self):
        self.assertEqual(str(self.orden), 'Pendiente')

    def test_verbose_name(self):
        self.assertEqual(Orden._meta.verbose_name, 'Orden')

    def test_verbose_name_plural(self):
        self.assertEqual(Orden._meta.verbose_name_plural, 'Ordenes')
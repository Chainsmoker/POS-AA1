from django.test import TestCase
from .models import Productos

class ProductosTestCase(TestCase):
    def setUp(self):
        self.producto = Productos(
            nombre='Producto de prueba',
            descripcion='Este es un producto de prueba',
            precio=19.99,
            stock=10,
            imagen=None
        )
        self.producto.save()

    def test_nombre_producto(self):
        self.assertEqual(self.producto.nombre, 'Producto de prueba')

    def test_descripcion_producto(self):
        self.assertEqual(self.producto.descripcion, 'Este es un producto de prueba')

    def test_precio_producto(self):
        self.assertEqual(self.producto.precio, 19.99)

    def test_stock_producto(self):
        self.assertEqual(self.producto.stock, 10)

    def test_imagen_producto(self):
        self.assertIsNone(self.producto.imagen)

    def test_str_producto(self):
        self.assertEqual(str(self.producto), 'Producto de prueba')

    def test_verbose_name(self):
        self.assertEqual(Productos._meta.verbose_name, 'Producto')

    def test_verbose_name_plural(self):
        self.assertEqual(Productos._meta.verbose_name_plural, 'Productos')
from django.test import TestCase
from .models import Descuentos

class DescuentosTestCase(TestCase):
    def setUp(self):
        self.descuento = Descuentos(
            titulo='Descuento de prueba',
            descripcion='Este es un descuento de prueba',
            porcentaje=10.00,
            fecha_inicio='2022-01-01',
            fecha_fin='2022-01-31'
        )
        self.descuento.save()

    def test_titulo_descuento(self):
        self.assertEqual(self.descuento.titulo, 'Descuento de prueba')

    def test_descripcion_descuento(self):
        self.assertEqual(self.descuento.descripcion, 'Este es un descuento de prueba')

    def test_porcentaje_descuento(self):
        self.assertEqual(self.descuento.porcentaje, 10.00)

    def test_fecha_inicio_descuento(self):
        self.assertEqual(self.descuento.fecha_inicio, '2022-01-01')

    def test_fecha_fin_descuento(self):
        self.assertEqual(self.descuento.fecha_fin, '2022-01-31')

    def test_creado_and_actualizado_are_not_none(self):
        self.assertIsNotNone(self.descuento.creado)
        self.assertIsNotNone(self.descuento.actualizado)

    def test_str_descuento(self):
        self.assertEqual(str(self.descuento), 'Descuento de prueba')

    def test_verbose_name(self):
        self.assertEqual(Descuentos._meta.verbose_name, 'Descuento')

    def test_verbose_name_plural(self):
        self.assertEqual(Descuentos._meta.verbose_name_plural, 'Descuentos')
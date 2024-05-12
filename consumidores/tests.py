from django.test import TestCase
from .models import Consumidores

class ConsumidoresTestCase(TestCase):
    def setUp(self):
        self.consumidor = Consumidores(
            nombre='Juan',
            apellido='Pérez',
            email='juanperez@example.com',
            telefono='1234567890',
            pais='España',
            ciudad='Madrid',
            direccion='Calle de la Paz, 12'
        )
        self.consumidor.save()

    def test_nombre_consumidor(self):
        self.assertEqual(self.consumidor.nombre, 'Juan')

    def test_apellido_consumidor(self):
        self.assertEqual(self.consumidor.apellido, 'Pérez')

    def test_email_consumidor(self):
        self.assertEqual(self.consumidor.email, 'juanperez@example.com')

    def test_telefono_consumidor(self):
        self.assertEqual(self.consumidor.telefono, '1234567890')

    def test_pais_consumidor(self):
        self.assertEqual(self.consumidor.pais, 'España')

    def test_ciudad_consumidor(self):
        self.assertEqual(self.consumidor.ciudad, 'Madrid')

    def test_direccion_consumidor(self):
        self.assertEqual(self.consumidor.direccion, 'Calle de la Paz, 12')

    def test_created_at_and_updated_at_are_not_none(self):
        self.assertIsNotNone(self.consumidor.created_at)
        self.assertIsNotNone(self.consumidor.updated_at)

    def test_str_consumidor(self):
        self.assertEqual(str(self.consumidor), 'Juan Pérez')

    def test_verbose_name(self):
        self.assertEqual(Consumidores._meta.verbose_name, 'Consumidor')

    def test_verbose_name_plural(self):
        self.assertEqual(Consumidores._meta.verbose_name_plural, 'Consumidores')
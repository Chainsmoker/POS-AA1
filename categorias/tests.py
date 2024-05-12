from django.test import TestCase
from .models import Categorias

class CategoriasTestCase(TestCase):
    def setUp(self):
        self.categoria = Categorias(
            nombre='Categoria de prueba',
            descripcion='Esta es una categoría de prueba'
        )
        self.categoria.save()

    def test_nombre_categoria(self):
        self.assertEqual(self.categoria.nombre, 'Categoria de prueba')

    def test_descripcion_categoria(self):
        self.assertEqual(self.categoria.descripcion, 'Esta es una categoría de prueba')

    def test_creado_and_actualizado_are_not_none(self):
        self.assertIsNotNone(self.categoria.creado)
        self.assertIsNotNone(self.categoria.actualizado)

    def test_str_categoria(self):
        self.assertEqual(str(self.categoria), 'Categoria de prueba')

    def test_verbose_name(self):
        self.assertEqual(Categorias._meta.verbose_name, 'Categoria')

    def test_verbose_name_plural(self):
        self.assertEqual(Categorias._meta.verbose_name_plural, 'Categorias')
# Generated by Django 5.0.6 on 2024-06-05 20:00

import django.db.models.deletion
import ordenes.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('descuentos', '__first__'),
        ('productos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('sub_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.productos')),
            ],
            options={
                'verbose_name': 'Orden Producto',
                'verbose_name_plural': 'Ordenes Productos',
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.UUIDField(default=ordenes.models.generate_order_id, editable=False, primary_key=True, serialize=False)),
                ('order_number', models.CharField(default=ordenes.models.generate_order_number, editable=False, max_length=32, unique=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en camino', 'En camino'), ('entregado', 'Entregado')], default='pendiente', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('consumidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('descuento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='descuentos.descuentos')),
                ('orden_producto', models.ManyToManyField(to='ordenes.ordenproducto')),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
            },
        ),
    ]

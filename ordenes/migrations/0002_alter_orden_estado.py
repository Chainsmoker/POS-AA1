# Generated by Django 5.0.6 on 2024-06-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.CharField(choices=[('no pagado', 'No pagado'), ('pendiente', 'Pendiente'), ('en camino', 'En camino'), ('entregado', 'Entregado')], default='no pagado', max_length=20),
        ),
    ]

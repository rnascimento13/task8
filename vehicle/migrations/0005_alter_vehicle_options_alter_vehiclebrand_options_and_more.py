# Generated by Django 5.0.3 on 2024-03-21 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_alter_vehicle_color_alter_vehicle_condition_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name': 'Veículo', 'verbose_name_plural': 'Veículos'},
        ),
        migrations.AlterModelOptions(
            name='vehiclebrand',
            options={'verbose_name': 'Marca do veículo', 'verbose_name_plural': 'Marcas dos veículos'},
        ),
        migrations.AlterModelOptions(
            name='vehiclecolor',
            options={'verbose_name': 'Cor', 'verbose_name_plural': 'Cores'},
        ),
        migrations.AlterModelOptions(
            name='vehiclecondition',
            options={'verbose_name': 'Condição do veículo', 'verbose_name_plural': 'Condições dos veículos'},
        ),
        migrations.AlterModelOptions(
            name='vehiclemodel',
            options={'verbose_name': 'Modelo', 'verbose_name_plural': 'Modelos'},
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20170615_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='city',
        ),
        migrations.AlterModelOptions(
            name='apartment',
            options={'verbose_name': 'Apartamento', 'verbose_name_plural': 'Apartamentos'},
        ),
        migrations.AlterModelOptions(
            name='commercial',
            options={'verbose_name': 'Ponto Comercial', 'verbose_name_plural': 'Pontos Comerciais'},
        ),
        migrations.AlterModelOptions(
            name='house',
            options={'verbose_name': 'Casa', 'verbose_name_plural': 'Casas'},
        ),
        migrations.AlterModelOptions(
            name='land',
            options={'verbose_name': 'Terreno', 'verbose_name_plural': 'Terrenos'},
        ),
        migrations.AlterField(
            model_name='apartment',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties_apartment', to='locations.City', verbose_name='cidade'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties_apartment', to='locations.Neighborhood', verbose_name='bairro'),
        ),
        migrations.AlterField(
            model_name='commercial',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties_commercial', to='locations.City', verbose_name='cidade'),
        ),
        migrations.AlterField(
            model_name='commercial',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties_commercial', to='locations.Neighborhood', verbose_name='bairro'),
        ),
        migrations.AlterField(
            model_name='house',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties_house', to='locations.City', verbose_name='cidade'),
        ),
        migrations.AlterField(
            model_name='house',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties_house', to='locations.Neighborhood', verbose_name='bairro'),
        ),
        migrations.AlterField(
            model_name='land',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties_land', to='locations.City', verbose_name='cidade'),
        ),
        migrations.AlterField(
            model_name='land',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties_land', to='locations.Neighborhood', verbose_name='bairro'),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Neighborhood',
        ),
    ]

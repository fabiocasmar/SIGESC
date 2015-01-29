# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import entidades.models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proponente',
            fields=[
                ('tipo_prop', models.CharField(max_length=15, choices=[('E', 'Estudiante'), ('P', 'Profesor'), ('C', 'Comunidad')])),
                ('id', models.CharField(primary_key=True, serialize=False, max_length=8)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('sexo', models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])),
                ('telefono', models.CharField(max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='USBID',
            field=models.CharField(primary_key=True, serialize=False, validators=[entidades.models.validarCarnet], max_length=8),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='carrera',
            field=models.CharField(max_length=4, choices=[('0800', 'Ing. Computacion'), ('0100', 'Ing. Mecanica'), ('0200', 'Ing. Electrica'), ('0300', 'Ing. Electronica'), ('0400', 'Ing. Produccion'), ('0500', 'Ing. Materiales'), ('0600', 'Ing. Quimica'), ('0700', 'Ing. Geofisica')]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(max_length=75),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='sede',
            field=models.CharField(max_length=1, choices=[('S', 'Sartenejas'), ('L', 'Litoral')]),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='estado',
            field=models.CharField(max_length=10, choices=[('A', 'Abierto'), ('C', 'Cerrado'), ('P', 'En Proceso')]),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='USBID',
            field=models.EmailField(primary_key=True, serialize=False, max_length=75),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='sede',
            field=models.CharField(max_length=1, choices=[('S', 'Sartenejas'), ('L', 'Litoral')]),
        ),
    ]

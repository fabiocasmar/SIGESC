# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursa',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('estado', models.CharField(choices=[('R', 'Retirado'), ('C', 'En curso'), ('F', 'Finalizado')], max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('USBID', models.CharField(serialize=False, max_length=8, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('cedula', models.CharField(max_length=8)),
                ('carrera', models.CharField(max_length=30)),
                ('sede', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('telefono', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cursa',
            name='estudiante',
            field=models.ForeignKey(to='entidades.Estudiante'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('cod_proyecto', models.CharField(serialize=False, max_length=7, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=40)),
                ('estado', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cursa',
            name='proyecto',
            field=models.ForeignKey(to='entidades.Proyecto'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('USBID', models.CharField(serialize=False, max_length=20, primary_key=True)),
                ('cedula', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('sede', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('telefono', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='tutor',
            field=models.ForeignKey(to='entidades.Tutor'),
            preserve_default=True,
        ),
    ]

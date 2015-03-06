# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0002_auto_20150128_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('nombre_area', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('nombre_sede', models.CharField(max_length=15, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='sede',
            field=models.ForeignKey(to='entidades.Sede'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='area',
            field=models.ForeignKey(to='entidades.Area'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutor',
            name='sede',
            field=models.ForeignKey(to='entidades.Sede'),
            preserve_default=True,
        ),
    ]

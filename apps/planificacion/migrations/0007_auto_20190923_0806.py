# Generated by Django 2.2.3 on 2019-09-23 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificacion', '0006_auto_20190923_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planificacion',
            name='planificacion_semestre',
            field=models.IntegerField(choices=[('Primero', '1'), ('Segundo', '2')]),
        ),
    ]

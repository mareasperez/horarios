# Generated by Django 2.2.3 on 2019-09-23 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planificacion', '0004_auto_20190903_0019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='planificacion',
            options={'ordering': ['planificacion_anyo_lectivo'], 'verbose_name': 'Planificacion', 'verbose_name_plural': 'Planificaciones'},
        ),
    ]

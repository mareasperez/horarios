# Generated by Django 2.2.3 on 2019-11-19 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planificacion', '0010_auto_20190923_0819'),
        ('docentes', '0005_auto_20191102_0306'),
        ('grupos', '0008_auto_20191119_0147'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='grupo',
            unique_together={('grupo_numero', 'grupo_planificacion', 'grupo_docente')},
        ),
    ]
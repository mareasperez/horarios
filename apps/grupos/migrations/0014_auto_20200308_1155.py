# Generated by Django 2.2.3 on 2020-03-08 17:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('planificacion', '0012_auto_20200214_0334'),
        ('componentes', '0014_auto_20191123_0328'),
        ('grupos', '0013_auto_20200227_2007'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='grupo',
            unique_together={('grupo_numero', 'grupo_planificacion', 'grupo_tipo', 'grupo_componente')},
        ),
    ]

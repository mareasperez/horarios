# Generated by Django 2.2.3 on 2019-11-22 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('componentes', '0011_auto_20191122_0614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='componente',
            options={'ordering': ['-componente_ciclo', '-componente_nombre']},
        ),
    ]

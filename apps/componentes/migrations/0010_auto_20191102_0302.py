# Generated by Django 2.2.3 on 2019-11-02 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('componentes', '0009_auto_20191102_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='componente_credito',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
    ]
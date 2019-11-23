# Generated by Django 2.2.3 on 2019-11-02 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('componentes', '0008_auto_20191102_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='componente_ciclo',
            field=models.IntegerField(choices=[(1, 'Ciclo 1'), (2, 'Ciclo 2'), (3, 'Ciclo 3'), (4, 'Ciclo 4'), (5, 'Ciclo 5'), (6, 'Ciclo 6'), (7, 'Ciclo 7'), (8, 'Ciclo 8'), (9, 'Ciclo 9'), (10, 'Ciclo 10')], default=1),
        ),
        migrations.AlterField(
            model_name='componente',
            name='componente_credito',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
    ]
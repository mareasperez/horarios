# Generated by Django 2.2.7 on 2020-10-16 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horario', '0016_auto_20201007_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='horario_vacio',
            field=models.BooleanField(default=False),
        ),
    ]

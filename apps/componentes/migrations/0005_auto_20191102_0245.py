# Generated by Django 2.2.3 on 2019-11-02 02:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('componentes', '0004_componente_componente_credito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='componente_ciclo',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
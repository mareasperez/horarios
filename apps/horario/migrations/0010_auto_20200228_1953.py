# Generated by Django 2.2.3 on 2020-02-29 01:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('horario', '0009_auto_20190903_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='horario_grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo'),
        ),
    ]

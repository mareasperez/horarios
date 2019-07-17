# Generated by Django 2.2.2 on 2019-06-14 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recintos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('aula_nombre', models.CharField(max_length=50)),
                ('aula_id', models.IntegerField(primary_key=True, serialize=False)),
                ('aula_tipo', models.IntegerField(default=0)),
                ('aula_capacidad', models.IntegerField(default=0)),
                ('aula_recinto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recintos.Recinto')),
            ],
        ),
    ]

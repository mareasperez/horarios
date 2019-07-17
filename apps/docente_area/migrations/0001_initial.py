# Generated by Django 2.2.2 on 2019-06-14 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('docentes', '0001_initial'),
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocenteArea',
            fields=[
                ('da_id', models.IntegerField(primary_key=True, serialize=False)),
                ('da_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area.Area')),
                ('da_docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Docente')),
            ],
        ),
    ]

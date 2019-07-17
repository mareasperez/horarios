# Generated by Django 2.2.2 on 2019-06-14 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planificacion', '0001_initial'),
        ('componentes', '0001_initial'),
        ('docentes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('grupo_id', models.IntegerField(primary_key=True, serialize=False)),
                ('grupo_numero', models.IntegerField(default=1)),
                ('grupo_max_capacidad', models.IntegerField(default=0)),
                ('grupo_tipo', models.CharField(default='teorico', max_length=50)),
                ('grupo_horas_clase', models.IntegerField(default=0)),
                ('grupo_modo', models.CharField(default='propiafacultad', max_length=50)),
                ('grupo_componente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='componentes.Componente')),
                ('grupo_docente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='docentes.Docente')),
                ('grupo_planificacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='planificacion.Planificacion')),
            ],
            options={
                'unique_together': {('grupo_numero', 'grupo_planificacion', 'grupo_docente', 'grupo_modo')},
            },
        ),
    ]

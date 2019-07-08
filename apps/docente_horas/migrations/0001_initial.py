# Generated by Django 2.2.2 on 2019-06-14 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planificacion', '0001_initial'),
        ('docentes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocenteHoras',
            fields=[
                ('dh_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dh_horas_asi', models.IntegerField()),
                ('dh_docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Docente')),
                ('dh_planificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planificacion.Planificacion')),
            ],
        ),
    ]
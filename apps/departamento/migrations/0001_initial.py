# Generated by Django 2.2.2 on 2019-06-14 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facultades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('departamento_nombre', models.CharField(max_length=50)),
                ('departamento_id', models.IntegerField(primary_key=True, serialize=False)),
                ('departamento_facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facultades.Facultad')),
            ],
        ),
    ]

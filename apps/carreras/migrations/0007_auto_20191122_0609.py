# Generated by Django 2.2.3 on 2019-11-22 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0006_auto_20191122_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='carrera_departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.Departamento'),
        ),
    ]
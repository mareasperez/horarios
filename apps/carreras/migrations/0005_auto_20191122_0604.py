# Generated by Django 2.2.3 on 2019-11-22 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0004_carrera_carrera_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='carrera_tipo',
            field=models.CharField(choices=[('P', 'Presencial'), ('V', 'Virtual')], default='p', max_length=1),
        ),
    ]
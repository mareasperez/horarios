# Generated by Django 2.2.2 on 2019-06-19 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan_de_estudio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plandeestudio',
            options={'ordering': ['-pde_id'], 'verbose_name': 'Plan de estudio', 'verbose_name_plural': 'Planes de estudio'},
        ),
    ]
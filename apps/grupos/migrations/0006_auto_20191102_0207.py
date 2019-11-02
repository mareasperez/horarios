# Generated by Django 2.2.3 on 2019-11-02 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0005_auto_20190923_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='grupo_modo',
            field=models.CharField(choices=[('S', 'Servicio'), ('F', 'Facultad')], default='S', max_length=50),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='grupo_tipo',
            field=models.CharField(choices=[('GT', 'Teorico'), ('GP', 'Practico')], default='GT', max_length=50),
        ),
    ]

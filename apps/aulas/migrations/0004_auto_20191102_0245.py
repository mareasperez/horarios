# Generated by Django 2.2.3 on 2019-11-02 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0003_auto_20190903_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='aula_tipo',
            field=models.BooleanField(default=0),
        ),
    ]

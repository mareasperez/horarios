# Generated by Django 2.2.3 on 2019-07-19 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='aula_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

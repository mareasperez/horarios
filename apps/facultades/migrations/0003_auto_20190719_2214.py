# Generated by Django 2.2.3 on 2019-07-19 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultades', '0002_auto_20190619_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultad',
            name='facultad_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

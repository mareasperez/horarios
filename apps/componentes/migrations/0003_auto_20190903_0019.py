# Generated by Django 2.2.3 on 2019-09-03 00:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('componentes', '0002_auto_20190719_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='componente',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='componente',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
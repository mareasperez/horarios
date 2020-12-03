# Generated by Django 2.2.7 on 2020-10-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horario', '0015_horario_horario_vacio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='horario_hora',
            field=models.IntegerField(choices=[(7, '7:00 am'), (8, '8:00 am'), (9, '9:00 am'), (10, '10:00 am'), (11, '11:00 am'), (12, '12:00 pm'), (13, '1:00 pm'), (14, '2:00 pm'), (15, '3:00 pm'), (16, '4:00 pm'), (17, '5:00 pm'), (18, '6:00 pm')], default=7),
        ),
    ]
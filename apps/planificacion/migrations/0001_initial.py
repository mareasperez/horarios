# Generated by Django 2.2.2 on 2019-06-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planificacion',
            fields=[
                ('planificacion_id', models.IntegerField(primary_key=True, serialize=False)),
                ('planificacion_anyo_lectivo', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=2019)),
                ('planificacion_semestre', models.CharField(choices=[('1', 'Primero'), ('2', 'Segundo')], max_length=50)),
            ],
        ),
    ]

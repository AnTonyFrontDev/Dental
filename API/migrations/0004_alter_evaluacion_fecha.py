# Generated by Django 4.2.1 on 2023-05-18 14:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_alter_evaluacion_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='fecha',
            field=models.DateField(db_column='Fecha', default=django.utils.timezone.now),
        ),
    ]

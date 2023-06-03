# Generated by Django 4.1.3 on 2023-05-18 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_alter_evaluacion_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta_Evaluacion',
            fields=[
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('fk_ev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.evaluacion')),
                ('fk_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.pregunta')),
            ],
            options={
                'db_table': 'Pregunta_Evaluacion',
            },
        ),
    ]

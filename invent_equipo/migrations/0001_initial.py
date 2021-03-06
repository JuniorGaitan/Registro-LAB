# Generated by Django 3.2 on 2021-05-07 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogos', '0005_rename_colore_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.CharField(max_length=70)),
                ('serie', models.CharField(max_length=70)),
                ('cod_inventario', models.IntegerField()),
                ('descripcion', models.CharField(max_length=70)),
                ('color_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.color')),
                ('estado_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.estado')),
                ('laboratorio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.laboratorio')),
                ('modelo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.modelo')),
            ],
        ),
    ]

# Generated by Django 3.2 on 2021-05-06 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0004_rename_colores_colore'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Colore',
            new_name='Color',
        ),
    ]

# Generated by Django 3.2.12 on 2022-09-21 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0002_materia_assunto'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]

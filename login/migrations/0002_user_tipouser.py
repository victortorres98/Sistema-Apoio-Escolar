# Generated by Django 3.2.12 on 2022-10-12 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tipoUser',
            field=models.CharField(default='ALUNO', max_length=256),
        ),
    ]
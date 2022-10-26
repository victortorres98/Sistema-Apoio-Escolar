# Generated by Django 3.2.12 on 2022-10-25 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_tipouser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('cash', models.DecimalField(decimal_places=2, default=1000000, max_digits=12)),
                ('init', models.DecimalField(decimal_places=2, default=1000000, max_digits=12)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Professor',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='tipoUser',
        ),
    ]
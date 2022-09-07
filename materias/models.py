from django.db import models

# Create your models here.
class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(unique=True, max_length=128)
    link = models.URLField(blank=False, null=False, max_length=256)
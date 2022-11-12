from audioop import reverse
from django.utils.text import slugify
from django.db import models

# Create your models here.
class Materia(models.Model):
    nome = models.CharField(unique=True, max_length=128)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Assunto(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nome = models.CharField(unique=True, max_length=128)
    link = models.URLField(blank=False, null=False, max_length=256)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Agenda(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    tarefa= models.CharField(unique=False, max_length=128)
    data = models.DateField()

    def __str__(self):
        return self.tarefa

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
from audioop import reverse
from django.utils.text import slugify
from django.db import models

# Create your models here.
class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(unique=True, max_length=128)
    assunto = models.CharField(max_length=128, default='0')
    slug = models.SlugField(unique=True, blank=True, null=True)
    link = models.URLField(blank=False, null=False, max_length=256)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug
            print(self.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

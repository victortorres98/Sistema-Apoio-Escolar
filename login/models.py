from django.db import models

# Create your models here.

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=128)
    email = models.EmailField(unique=True)
    password = models.CharField(blank=False, null=False, max_length=256)
    cash = models.DecimalField(max_digits=12, decimal_places=2, default=1000000)
    init = models.DecimalField(max_digits=12, decimal_places=2, default=1000000)
    createdAt = models.DateTimeField(auto_now_add=True)
    tipo_user = models.CharField(blank=False, null=False, max_length=256, default='ALUNO')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Alunos'

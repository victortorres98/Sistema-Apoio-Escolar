from django.contrib import admin
from materias.models import *

# Register your models here.

class ListandoMaterias(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(Materia, ListandoMaterias)
admin.site.register(Assunto)
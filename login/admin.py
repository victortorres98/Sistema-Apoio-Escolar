from django.contrib import admin

# Register your models here.
from login.models import *

class ListandoUser(admin.ModelAdmin):
    
    search_fields = ('username',)

admin.site.register(Aluno)

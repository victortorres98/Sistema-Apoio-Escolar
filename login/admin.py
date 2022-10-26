from django.contrib import admin

# Register your models here.
from login.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'createdAt')

class ListandoAlunos(admin.ModelAdmin):
    list_display = ('username', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', '')


admin.site.register(User, UserAdmin)
admin.site.register(Professor)
admin.site.register(Aluno)

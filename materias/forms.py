from django import forms
from .models import *

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ["nome", "link"]

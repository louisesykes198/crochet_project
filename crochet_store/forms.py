from django import forms
from .models import CrochetItem

class CrochetItemForm(forms.ModelForm):
    class Meta:
        model = CrochetItem
        fields = ['name', 'description', 'image', 'price']

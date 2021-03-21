from django import forms

from .models import *

class ProductForms(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
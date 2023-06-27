from django import forms
from .models import Collection
class Col_Form(forms.ModelForm):
    class Meta:
        model=Collection
        fields='__all__'
        widgets={'name': forms.TextInput(attrs={'required': False})}
        labels={'name':'Enter your Name', 'age':"Enter your Age"}

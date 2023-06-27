from django import forms
from .models import DairyMembers

class DairyRegister(forms.ModelForm):
    class Meta():
        model=DairyMembers
        fields="__all__"



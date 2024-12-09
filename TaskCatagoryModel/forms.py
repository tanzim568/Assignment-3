from django import forms
from .models import TaskCatergory   


class CatagoryForm(forms.ModelForm):
    class Meta:
        model=TaskCatergory
        fields='__all__'


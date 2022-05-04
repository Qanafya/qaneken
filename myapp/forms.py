from django import forms
from .models import *

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

class QoldanForm(forms.ModelForm):
    class Meta:
        model = Qoldan
        fields = ['login', 'name', 'surname', 'email', 'age', 'country', 'password', 'confirm']
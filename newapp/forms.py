from newapp.models import Login
from django import forms

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=['username','password']
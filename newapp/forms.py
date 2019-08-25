from newapp.models import Login,Student
from django import forms

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=['username','password']

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','email','rollno']
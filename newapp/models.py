from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=128)
    password=models.CharField(max_length=128)

class Student(models.Model):
    name=models.CharField(max_length=128)
    email=models.EmailField()
    rollno=models.CharField(max_length=16)


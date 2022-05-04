from django.db import models
from django.core.validators import RegexValidator

alpha = RegexValidator(r'^[a-zA-Z]*$', 'Numbers not allowed.')
# Create your models here.

class Eltanba(models.Model):
    jyl = models.CharField(max_length=15)
    aty = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    link = models.CharField(max_length=200)

class Ramiz(models.Model):
    aty = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    to_link = models.CharField(max_length=200)


class Anuran(models.Model):
    jyl = models.CharField(max_length=200)
    soz = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

class Users(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Qoldan(models.Model):
    login = models.CharField(max_length=255, validators=[alpha])
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    country = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm = models.CharField(max_length=255)
    em_pass = models.CharField(max_length=255)

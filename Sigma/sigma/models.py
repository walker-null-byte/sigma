import chardet
from django.db import models
from django.forms import CharField

# Create your models here.
class signup(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    passw = models.CharField(max_length=50)
    


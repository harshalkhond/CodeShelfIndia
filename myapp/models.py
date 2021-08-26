from os import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    username=models.CharField(max_length=20,default='username')
    name=models.CharField(max_length=122)
    password=models.CharField(max_length=12)
    number=models.CharField(max_length=20)
    email=models.CharField(max_length=40,default="email")

    def __str__(self):
        return self.name
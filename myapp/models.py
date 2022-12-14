from os import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    username=models.CharField(max_length=30,default='username')
    password=models.CharField(max_length=12)
    number=models.CharField(max_length=20)
    email=models.CharField(max_length=40,default="email")
    feedback=models.CharField(max_length=50,default="Feedback")
    def __str__(self):
        return self.username
class Feedback(models.Model):
    name=models.CharField(max_length=122)
    feedback=models.CharField(max_length=150)
    suggestion=models.CharField(max_length=150)
    def __str__(self):
        return self.name
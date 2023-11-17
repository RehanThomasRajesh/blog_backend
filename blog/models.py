from django.db import models

# Create your models here.
class user(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=20)
    profile = models.CharField(max_length=2000)
    email = models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class post(models.Model):
    title = models.CharField(max_length=50)
    id= models.CharField(max_length=100,primary_key=True)
    message=models.CharField(max_length=5000)

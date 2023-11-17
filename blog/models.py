from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=20)
    profile = models.CharField(max_length=2000)
    email = models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class post(models.Model):
    title = models.CharField(max_length=50)
    user_id= models.CharField(max_length=100,default="")
    message=models.CharField(max_length=5000)

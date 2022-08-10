from django.db import models

# Create your models here.

class Customer(models.Model):
    name= models.CharField(max_length=100)
    phNo= models.CharField(max_length=50)
    address= models.CharField(max_length=255)
    birthDay= models.DateField(auto_created=False,auto_now_add=False,auto_now=False)
    gender= models.CharField(max_length=50)
    item= models.CharField(max_length=50)

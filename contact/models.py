from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=10)
    address=models.CharField(max_length=20)
    mobile=models.IntegerField()
    message=models.CharField(max_length=40, default='')
    gender=models.CharField(max_length=1,default='')
    country=models.CharField(max_length=100,default='')

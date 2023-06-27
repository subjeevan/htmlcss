from django.db import models

# Create your models here.

class Members(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    fullname=models.CharField(max_length=20)
    address=models.CharField(max_length=20)

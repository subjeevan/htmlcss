from django.db import models

# Create your models here.

class DairyMembers(models.Model):
    memb_fname=models.CharField(max_length=10)
    memb_lname=models.CharField(max_length=10)
    memb_fullname=models.CharField(max_length=10)
    memb_age=models.IntegerField()
    memb_address=models.CharField(max_length=10)
    memb_image=models.ImageField(upload_to='membimage')
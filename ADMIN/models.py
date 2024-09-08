from django.db import models

# Create your models here.
class doctorlist(models.Model):
    doctorphoto=models.ImageField(max_length=200)
    doctorname=models.CharField(max_length=200)
    doctoremail=models.CharField(max_length=200)
    # doctorphone=models.IntegerField(max_length=200)
    doctorqualification=models.CharField(max_length=200)
    enterdutystarttime=models.CharField(max_length=200)
    # enterdutyendtime=models.CharField(max_length=200)
    anysuggestion=models.CharField(max_length=200)

class userdetails(models.Model):
    userphoto=models.ImageField()
    username=models.CharField(max_length=200)
    useremail=models.CharField(max_length=200)
    userphone=models.CharField(max_length=200)
    userpassword=models.CharField(max_length=200)
    



         

  
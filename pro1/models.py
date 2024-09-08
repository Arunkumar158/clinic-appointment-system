from django.db import models


class details(models.Model):
    photo=models.ImageField()
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    
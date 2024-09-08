from django.db import models

# Create your models here.

class appointments(models.Model):
    patient_name=models.CharField(max_length=200)
    patient_email=models.CharField(max_length=200)
    patient_mobile=models.CharField(max_length=200)
    patient_doctor=models.CharField(max_length=200)
    patient_date=models.CharField(max_length=200)
    patient_problem=models.CharField(max_length=200)
    
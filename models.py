from django.db import models

# Create your models here.

class Personal_information(models.Model):
    Name=models.CharField(max_length=30)
    Father_Name=models.CharField(max_length=20)
    Mother_Name=models.CharField(max_length=25)
    DateOfBirth=models.DateTimeField()
    Gender=models.CharField(max_length=7)
    Native_District=models.CharField(max_length=25)
    Martial_status=models.CharField(max_length=20)
    Language_known=models.CharField(max_length=20)
    Higher_Qualification=models.CharField(max_length=20)
    Project=models.CharField(max_length=20)
    Permanaent_address=models.CharField(max_length=20)
    phone_number=models.IntegerField()
    EmailID=models.EmailField(max_length = 70)

def __str__(self):
    return "Personal_information" + Name

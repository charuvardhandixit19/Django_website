from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    password= models.CharField(max_length=50)
    Phone = models.CharField(max_length=20) 
    Suggetion = models.TextField()
    date = models.DateField()
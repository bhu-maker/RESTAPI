from django.db import models

# Create your models here.


class corporates(models.Model):
    org=models.CharField(max_length=200)
    nature=models.CharField(max_length=200)
    opennings=models.TextField()
    salary=models.DecimalField(max_digits=3,decimal_places=2)
    employees=models.IntegerField()
    ratings=models.DecimalField(max_digits=3,decimal_places=2)


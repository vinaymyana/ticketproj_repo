from django.db import models

# Create your models here.

class Location(models.Model):
    location=models.CharField(max_length=32)

class Theatre(models.Model):
    theatre=models.CharField(max_length=32)

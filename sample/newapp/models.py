from django.db import models

# Create your models here.
class Institutes(models.Model):
    name=models.CharField(max_length=100)
    registration_code=models.CharField(max_length=5)
    chancellor=models.CharField(max_length=50)

#
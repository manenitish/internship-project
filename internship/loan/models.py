from django.db import models

# Create your models here.

class empmodel(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    date = models.DateField(null=True)
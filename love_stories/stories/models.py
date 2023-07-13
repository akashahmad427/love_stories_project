from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=90)
    moral = models.CharField(max_length=200)
    story = models.TextField(max_length=5000)

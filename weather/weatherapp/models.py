from django.db import models

# Create your models here.

class WeatherModel(models.Model):
      city=models.CharField(max_length=200)



def __str__(self):
    return "city={0}".format(self.city)
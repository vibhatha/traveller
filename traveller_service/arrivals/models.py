from django.db import models

# Create your models here.

class Arrivals(models.Model):
    country = models.CharField(max_length=255)
    year = models.IntegerField()
    month = models.CharField(max_length=255)
    arrivals = models.IntegerField()

    def __str__(self):
        return f"{self.country} - {self.year} - {self.month}"
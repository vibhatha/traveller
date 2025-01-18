from django.db import models

class AllCountryStats(models.Model):
    country = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    month = models.CharField(max_length=10)
    passengers = models.IntegerField()

    def __str__(self):
        return f"{self.country} - {self.year}/{self.month}"

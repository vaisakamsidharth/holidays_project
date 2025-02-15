from django.db import models

# Create your models here.

class Holiday(models.Model):
    country = models.CharField(max_length=100)
    date = models.DateField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.country})"
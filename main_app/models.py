from django.db import models


# Create your models here.
class Workout(models.Model):
    split = models.CharField(max_length=50)
    date = models.DateField("Workout Date")
    notes = models.TextField(max_length=300)

    def __str__(self):
        return self.split

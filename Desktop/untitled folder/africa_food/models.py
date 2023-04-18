from django.db import models

# Create your models here.


class African_dishes(models.Model):
    """List of african dishes"""
    name = models.CharField(max_length=155)
    origin = models.CharField(max_length=155)
    preparation = models.TextField(max_length=155)
    cost = models.IntegerField()
    min_served = models.IntegerField()

    def __str__(self):
        """ return a string"""
        return f'The dish {self.name} comes from {self.country}'

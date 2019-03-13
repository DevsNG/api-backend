from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=200)
    capital = models.CharField(max_length=200)
    created_on = models.PositiveIntegerField()
    created_from = models.CharField(max_length=200, null=True, blank=True, default='N/A')
    governor = models.CharField(max_length=500)
    vice_governor = models.CharField(max_length=500, default='N/A', null=True, blank=True)
    geopolitical_zone = models.CharField(max_length=100)
    slogan = models.CharField(max_length=400)
    no_of_local_governments = models.PositiveIntegerField(default='N/A')
    denonyms = models.CharField(max_length=400, null=True, blank=True, default='N/A')
    landmarks = models.CharField(max_length=1000)
    website = models.URLField(null=True, blank=True, default='N/A')

    def __str__(self):
        return self.name
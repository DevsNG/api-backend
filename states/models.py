from django.db import models
from djchoices import ChoiceItem, DjangoChoices
# Create your models here.

class State(models.Model):
    class Zone(DjangoChoices):
        north_central = ChoiceItem('north_central', 'north central')
        north_east = ChoiceItem('north_east', 'north east')
        north_west = ChoiceItem('north_west', 'north west')
        south_east = ChoiceItem('south_east', 'south east')
        south_south = ChoiceItem('south_south', 'south south')
        south_west = ChoiceItem('south_west', 'south west')

    name = models.CharField(max_length=200)
    capital = models.CharField(max_length=200)
    created_on = models.PositiveIntegerField()
    created_from = models.CharField(max_length=200, null=True, blank=True, default='N/A')
    governor = models.CharField(max_length=500)
    deputy_governor = models.CharField(max_length=500, default='N/A', null=True, blank=True)
    geopolitical_zone = models.CharField(max_length=100, choices=Zone.choices)
    slogan = models.CharField(max_length=400)
    no_of_local_governments = models.PositiveIntegerField(default='N/A')
    denonyms = models.CharField(max_length=400, null=True, blank=True, default='N/A')
    # landmarks = models.CharField(max_length=1000)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
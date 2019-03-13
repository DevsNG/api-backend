from django.db import models

# Create your models here.
class Airport(models.Model):

    AIRPORT_TYPE = (
        ('domestic', 'domestic'),
        ('international', 'international')
    )

    name = models.CharField(max_length=500)
    # town = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    type = models.CharField(max_length=100, choices=AIRPORT_TYPE)
    established = models.PositiveIntegerField()
    website = models.URLField(blank=True, null=True, default='N/A')

    def __str__(self):
        return self.name
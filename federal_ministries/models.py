from django.db import models

# Create your models here.

class FederalMinistry(models.Model):
    full_name = models.CharField(max_length=400)
    short_name = models.CharField(max_length=20)
    description = models.TextField()
    established = models.PositiveSmallIntegerField(null=True)
    # logo = models.ImageField(upload_to='fed_min_logos', blank=True, null=True, default='N/A')
    current_minister = models.CharField(max_length=500)
    permanent_secretary = models.CharField(max_length=500, default='N\A')
    headquarters = models.CharField(max_length=100, default='Abuja')
    twitter = models.URLField(blank=True, null=True, default='N/A')
    website = models.URLField(blank=True, null=True, default='N/A')

    class Meta:
        verbose_name_plural = 'Federal Ministries'

    def __str__(self):
        return self.full_name

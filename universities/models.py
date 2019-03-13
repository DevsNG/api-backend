from django.db import models

# Create your models here.
class University(models.Model):

    UNIVERSITY_TYPE = (
        ('private', 'private'),
        ('state', 'state'),
        ('federal', 'federal')
    )


    full_name = models.CharField(max_length=300)
    nick_name = models.CharField(max_length=50)
    campuses = models.CharField(max_length=200, blank=True, null=True, default='N/A')
    established = models.PositiveIntegerField()
    # location = models.CharField(max_length=500)
    town = models.CharField(max_length=100, default='N/A')
    state = models.CharField(max_length=50, default='N/A')
    type = models.CharField(max_length=20, choices=UNIVERSITY_TYPE, default='')
    chancellor = models.CharField(max_length=400, blank=True, null=True, default='N/A')
    vice_chancellor = models.CharField(max_length=400)
    motto = models.CharField(max_length=300, blank=True, null=True, default='N/A')
    website = models.URLField(default='N/A')
    logo = models.ImageField(upload_to='university_logos', null=True, blank=True, default='N/A')

    class Meta:
        ordering = ('full_name', )
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.full_name




from django.db import models

from smithsonian.users.models import CustomUser


class Sighting(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             related_name='sightings')

    is_alive = models.BooleanField(default=False)
    cause_of_death = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=30, null=True)
    longitude = models.CharField(max_length=30, null=True)
    comment = models.TextField(null=True, blank=True)
    species = models.CharField(max_length=60, null=True, blank=True)


class SightingImage(models.Model):
    url = models.ImageField(upload_to='sightings/%Y/%m/%d', max_length=200)
    sighting = models.ForeignKey(Sighting, on_delete=models.CASCADE,
                                 related_name='images')

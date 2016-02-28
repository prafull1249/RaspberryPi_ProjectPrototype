from __future__ import unicode_literals

from django.db import models

# Create your models here.

class inverterAsu(models.Model):
    vendor = models.CharField(max_length=200)
    health = models.CharField(max_length=200)
    activeSince= models.DateTimeField('date published')
    temp = models.IntegerField(default=0)
    prod = models.IntegerField(default=0)
    switch = models.IntegerField(default=0)
    uptime = models.IntegerField(default=0)





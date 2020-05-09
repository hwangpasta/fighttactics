from django.contrib.postgres.fields import ArrayField
from django.db import models
# Create your models here.

class Champion(models.Model):
    name = models.CharField(max_length=254, default='Champion')
    championId = models.CharField(max_length=254, default='hm')
    cost = models.IntegerField(default=0)
    traits = ArrayField(models.CharField(max_length=254), blank=True)

    def __str__(self):
        return self.name

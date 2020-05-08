import json
from django.db import models

# Create your models here.

class Champion(models.Model):
    name = models.CharField(max_length=254, default='Champion')
    championId = models.CharField(max_length=254, default='hm')

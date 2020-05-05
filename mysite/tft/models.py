from django.db import models

# Create your models here.

class Champion(models.Model):
    champion_name = models.CharField(max_length=200)
from django.db import models
# Create your models here.

# The model has each of the champions attributes
class Champion(models.Model):
    objects = None
    name = models.CharField(max_length=254, default='Champion')
    championId = models.CharField(max_length=254, default='hm')
    cost = models.IntegerField(default=0)
    trait1 = models.CharField(max_length=254, default='Blank1')
    trait2 = models.CharField(max_length=254, default='Blank2')
    trait3 = models.CharField(max_length=254, default='Blank3')

    def __str__(self):
        return self.name

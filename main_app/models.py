from pydoc import describe
from unicodedata import name
from django.db import models
from django.urls import reverse

# Create your models here.
class Synth(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'synth_id':self.id}) 
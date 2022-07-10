from pydoc import describe
from unicodedata import name
from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
TIME = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)


class Synth(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.FloatField()

    def order_for_today(self):
        return self.order_set.filter(date=date.today().count() >= len(TIME))


class Order(models.Model):
    date = models.DateField('order date')
    time = models.CharField(
        max_length=1,
        choices=TIME,
        default=TIME[0][0]
    )
    synth = models.ForeignKey(Synth, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('detail', kwargs={'synth_id': self.id})
from django.contrib import admin
from .models import Synth, Order,Person
# Register your models here.

admin.site.register(Synth)
admin.site.register(Order)
admin.site.register(Person)
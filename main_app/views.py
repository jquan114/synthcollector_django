from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1> Hello </h1>')

def about(request):
    return render(request, 'about.html')

def synths_index(request):
    return render(request,'synths/index.html',{ 'synths': synths })

#Add the Synth class & list view function below the imports
class Synth:
    def __init__(self, name, brand, description, price):
        self.name = name
        self.brand = brand
        self.description = description
        self.price = price
synths = [
    Synth('PolyBrute','Arturia','6-voice analog',2699),
    Synth('Matriarch','Moog','Dark Semi-Modular',2100),
    Synth('Modewave','Korg','Wavetable',800),
  
]
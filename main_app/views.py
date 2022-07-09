from django.shortcuts import render
from django.http import HttpResponse
from .models import Synth
# Create your views here.

def home(request):
    return HttpResponse('<h1> Hello </h1>')

def about(request):
    return render(request, 'about.html')

def synths_index(request):
    synth = Synth.objects.all()
    return render(request,'synths/index.html',{ 'synths': synth })

def synths_detail(request, synth_id):
    synth = Synth.objects.get(id=synth_id)
    return render(request,'synths/detail.html', {'synth': synth})

#Add the Synth class & list view function below the imports

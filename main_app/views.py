from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Synth
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Synth
from .forms import OrderForm

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
    order_form = OrderForm()
    return render(request,'synths/detail.html', 
    {'synth': synth, 'order_form': order_form})

def add_order(request, synth_id):
    form = OrderForm(request.POST)
    if form.is_valid():
        new_order = form.save(commit=False)
        new_order.synth_id = synth_id
        new_order.save()
    return redirect('detail', synth_id=synth_id)


#Add the Synth class & list view function below the imports
class SynthCreate(CreateView):
    model = Synth
    fields = ['name','brand','description','price']
    success_url = '/synths/'

class SynthUpdate(UpdateView):
    model = Synth
    fields = ['name','brand','description','price']
    success_url = '/synths/'

class SynthDelete(DeleteView):
    model = Synth
    success_url= '/synths/'
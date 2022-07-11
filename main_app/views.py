from django.shortcuts import render, redirect
from .models import Synth
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Synth, Person
from .forms import OrderForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def synths_index(request):
    synth = Synth.objects.filter(user=request.user)
    return render(request,'synths/index.html',{ 'synths': synth })

@login_required
def synths_detail(request, synth_id):
    synth = Synth.objects.get(id=synth_id)
    persons_synth_doesnt_have = Person.objects.exclude(id__in = synth.persons.all().values_list('id'))
    order_form = OrderForm()
    return render(request,'synths/detail.html', 
    {'synth': synth, 'order_form': order_form,
    'persons':persons_synth_doesnt_have})

@login_required
def add_order(request, synth_id):
    form = OrderForm(request.POST)
    if form.is_valid():
        new_order = form.save(commit=False)
        new_order.synth_id = synth_id
        new_order.save()
    return redirect('detail', synth_id=synth_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


#Add the Synth class & list view function below the imports
class SynthCreate(LoginRequiredMixin,CreateView):
    model = Synth
    fields = ['name','brand','description','price']
    success_url = '/synths/'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SynthUpdate(LoginRequiredMixin,UpdateView):
    model = Synth
    fields = ['name','brand','description','price']
    success_url = '/synths/'

class SynthDelete(LoginRequiredMixin,DeleteView):
    model = Synth
    success_url= '/synths/'


from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('synths/',views.synths_index,name='index'),
    path('synths/<int:synth_id>/', views.synths_detail, name='detail'),
]
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy
class SchoolList(ListView):
    model=School
    context_object_name='schools'
    #template_name='app/School_list.html'
    #queryset=School.objects.filter(name='kvs')
    ordering=['name']

class home(TemplateView):
    template_name='app/home.html'


class SchoolDetails(DetailView):
    model=School
    context_object_name='s'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='s'
    success_url=reverse_lazy('SchoolList')
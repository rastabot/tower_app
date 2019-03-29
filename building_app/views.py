from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from . import models


# Create your views here.

class IndexView(TemplateView):
    template_name='index.html'

class BuildingListView(ListView):
    context_object_name = 'buildings'
    model = models.Building

class BuildingDetailView(DetailView):
    context_object_name = 'building'
    model = models.Building
    template_name = 'building_app/build_detail.html'

class AptListView(ListView):
    context_object_name =  'apts'
    model = models.Apartment

class AptDetailView(DetailView):
    context_object_name = 'apt'
    model = models.Apartment
    template = 'building_app/apt_detail.html'

class AptUpdateView(UpdateView):
    fields = ('extras',)
    model =  models.Apartment

class PersonListView(ListView):
    context_object_name = 'persons'
    model = models.Person
    template_name = 'building_app/persons_list.html'

class CreatePunchIn(CreateView):
    context_object_name = 'punchin'
    fields = ('person','start_time',)
    model = models.Punchclock
    template_name ='building_app/punchin.html'

class UpdatePunchOut(UpdateView):
    context_object_name = 'punchout'
    model = models.Punchclock
    template_name ='building_app/punchout.html'

class PunchclockDetailView(DetailView):
    context_object_name = 'punch_details'
    model = models.Punchclock
    template_name = 'building_app/punch_details.html'

    


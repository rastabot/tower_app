from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=100)
    num_of_apts = models.PositiveIntegerField()
    num_of_floors = models.PositiveIntegerField()
    elevator = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index/",kwargs={'pk':self.pk})


class Apartment(models.Model):
    extra_choices=(
        ('jacuzzi','jacuzzi'),
        ('sauna','sauna'),
        ('studio','studio'),
    )
    building_name =  models.ForeignKey(Building,on_delete=models.CASCADE,related_name='tower')
    family_name = models.CharField(max_length=100)
    num_of_rooms = models.PositiveIntegerField()
    parking_spot = models.BooleanField(default=True)
    extras = models.CharField(max_length=10,choices=extra_choices,default='studio')

    def get_absolute_url(self):
        return reverse('building_app:building',kwargs={'pk':self.building_name.pk })



class Person(models.Model):
    user= models.OneToOneField(User,on_delete="")

    def __str__(self):
        return self.user.username

class Punchclock(models.Model):
    person = models.ForeignKey(Person,on_delete="models.CASACADE",related_name='the_person',null=True)
    start_date = models.DateField(auto_now_add=True,null=True,blank=True, unique_for_date=True)
    start_time = models.TimeField(editable=True,null=True, blank=True)
    end_time = models.TimeField(editable=True,null=True, blank=True)


    def __str__(self):
        return self.start_time

    def get_absolute_url(self):
        return reverse('building_app:persons_list')
from django.contrib import admin
from building_app.models import Building,Apartment,Person,Punchclock

# Register your models here.
admin.site.register(Building)
admin.site.register(Apartment)
admin.site.register(Person)
admin.site.register(Punchclock)


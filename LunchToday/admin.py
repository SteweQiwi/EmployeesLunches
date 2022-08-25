from django.contrib import admin

from .models import *

admin.site.register(Restaurant)
admin.site.register(EmployeeCompany)
admin.site.register(EmployeeRestaurant)
admin.site.register(Lunch)

# Register your models here.

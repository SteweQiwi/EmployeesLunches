from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    kitchen = models.CharField(max_length=50, default='Asian')

    @property
    def votes(self):
        return EmployeeCompany.objects.filter(restaurant_id=self.id).count()


class EmployeeCompany(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, blank=True, null=True)


class EmployeeRestaurant(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Lunch(TimeStampedModel):
    first_course = models.CharField(max_length=100)
    main = models.CharField(max_length=100)
    dessert = models.CharField(max_length=100)
    drink = models.CharField(max_length=100)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)




# Create your models here.

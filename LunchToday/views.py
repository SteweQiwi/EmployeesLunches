from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from .serializers import *


class UploadMenuFromRestaurantView(generics.CreateAPIView):
    permission_classes = [IsRestaurant]
    serializer_class = LunchSerializer


class CreateEmployeeCompanyView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeCompanySerializer


class CreateRestaurantView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RestaurantSerializer


class CurrentDayMenu(generics.ListAPIView):
    permission_classes = [IsCompany]
    serializer_class = LunchSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        return Lunch.objects.filter(restaurant_id=restaurant_id)


class VotesView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsCompany]
    serializer_class = VotingSerializer

    def get_object(self):
        return EmployeeCompany.objects.get(user_id=self.request.user.id)


class ResultVotesView(generics.ListAPIView):
    permission_classes = [IsCompany]
    serializer_class = ResultSerializer

    def get_queryset(self):
        return Restaurant.objects.all()
# Create your views here.

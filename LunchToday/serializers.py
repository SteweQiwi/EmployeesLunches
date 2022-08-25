from rest_framework import serializers

from .models import *


class LunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lunch
        fields = ['first_course', 'main', 'dessert', 'drink', 'restaurant', 'id']
        read_only_fields = ['id']


class EmployeeCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCompany
        fields = ['id', 'name', 'restaurant']
        # read_only_fields = ['id']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'id', 'kitchen']
        read_only_fields = ['id']


class VotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCompany
        fields = ['restaurant']


class ResultSerializer(serializers.ModelSerializer):
    votes = serializers.ReadOnlyField()

    class Meta:
        model = Restaurant
        fields = ['name', 'kitchen', 'votes']

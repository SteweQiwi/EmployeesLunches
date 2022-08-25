import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from .models import *


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_user():
    return baker.make(User)


@pytest.fixture
def employee_restaurant():
    return baker.make(EmployeeRestaurant)


@pytest.fixture
def employee_restaurant_user(employee_restaurant):
    return employee_restaurant.user


@pytest.fixture
def restaurant():
    return baker.make(Restaurant)


@pytest.fixture
def employee_company():
    return baker.make(EmployeeCompany)


@pytest.fixture
def employee_company_user(employee_company):
    return employee_company.user


# @pytest.fixture
# def order(driver):
#     return baker.make('autopark.Order', driver=driver)


@pytest.fixture
def lunch():
    return baker.make(Lunch)


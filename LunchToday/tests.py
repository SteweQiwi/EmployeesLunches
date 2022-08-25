import pytest
from django.test import TestCase
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_upload_menu_from_restaurant(api_client, employee_restaurant_user, restaurant):
    api_client.force_authenticate(employee_restaurant_user)
    response = api_client.post(
        '/lunchtoday/upload-menu-from-restaurant/', {
            "first_course": 'soup',
            "main": 'kartoshka',
            "dessert": 'morog',
            "drink": 'voda',
            "restaurant": restaurant.pk,

        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) == 6


def test_create_employee_company(api_client, authenticated_user):
    api_client.force_authenticate(authenticated_user)
    response = api_client.post(
        '/lunchtoday/create-employee/', {"name": 'vitalya', "user": authenticated_user}
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) == 3


def test_create_restaurant(api_client, authenticated_user):
    api_client.force_authenticate(authenticated_user)
    response = api_client.post(
        '/lunchtoday/create-restaurant/', {"name": 'vitalya'}
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) == 3
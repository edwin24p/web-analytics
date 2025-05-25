import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestRegisterView:
    def setup_method(self):

        self.client = APIClient()
        # reverse looks for the url given the view name
        self.url = reverse("register")


    def test_register_user_success(self):

        data={
            "username":"testuser",
            "email":"test@example.com",
            "password":"strongpassword123",
            "password2":"strongpassword123"
        }
        response = self.client.post(self.url, data)
        assert response.status_code==201
        assert User.objects.filter(username="testuser").exists()

    def test_register_user_password_mismatch(self):
        data = {
            "username": "testuser2",
            "email": "test2@example.com",
            "password": "password123",
            "password2": "wrongpassword"
        }
        response = self.client.post(self.url, data)
        assert response.status_code == 400
        assert not User.objects.filter(username="testuser2").exists()

    def test_register_user_missing_username(self):
        data = {
            "email": "test3@example.com",
            "password": "password123",
            "password2": "password123"
        }
        response = self.client.post(self.url, data)
        assert response.status_code == 400

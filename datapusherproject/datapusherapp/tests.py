from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {"username": "testuser", "email": "test@example.com", "password": "testpass123"}

    def test_register_user(self):
        response = self.client.post('/api/register/', self.user_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)

    def test_login_user(self):
        User.objects.create_user(**self.user_data)
        response = self.client.post('/api/login/', {"username": "testuser", "password": "testpass123"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)

    def test_logout_user(self):
        user = User.objects.create_user(**self.user_data)
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/api/logout/')
        self.assertEqual(response.status_code, 200)

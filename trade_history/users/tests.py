import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import IntegrityError
from .serializers import UserSerializer

client = APIClient()

class GetAllUsersTest(TestCase):
    def setUp(self):
        User.objects.create(username='test1', email='test1@email.com')
        User.objects.create(username='test2', email='test2@email.com')
        User.objects.create(username='test3', email='test3@email.com')

    def test_get_all_users(self):
        response = client.get('/users/')
        serializer = UserSerializer(User.objects.all(), many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_repeat_username(self):
        with self.assertRaises(IntegrityError):
            User.objects.create(username='test1', email='test4@email.com')

class CreateNewUsers(TestCase):
    def setUp(self):
        self.payload = {
            'username':'test1',
            'email': 'test1@email.com',
            'password':'password'
        }
        self.same_user = {
            'username':'test1',
            'email': 'test10@email.com',
            'password':'password'
        }
        self.same_email = {
            'username':'test10',
            'email': 'test1@email.com',
            'password':'password'
        }
        self.missing_username = {
            'username':'',
            'email': 'test1@email.com',
            'password':'password'
        }
        self.missing_email = {
            'username':'test2',
            'email': '',
            'password':'password'
        }
        self.missing_password = {
            'username':'test3',
            'email': 'test3@email.com',
            'password':''
        }

    def test_create_new_user(self):
        response = client.post('/users/', self.payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_same_user_info(self):
        response = client.post('/users/', self.payload, format='json')
        response = client.post('/users/', self.same_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = client.post('/users/', self.same_email, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_user_info(self):
        response = client.post('/users/', self.missing_username, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = client.post('/users/', self.missing_email, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = client.post('/users/', self.missing_password, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)




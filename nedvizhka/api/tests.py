from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from sale.models import Flat
from api.serializers import FlatSerializer
from rest_framework_simplejwt.tokens import AccessToken


class FlatViewsTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='test', password='test')
        self.user2 = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.flat_data = {
            'title': 'Flat 1',
            'description': 'Description for Flat 1',
            'is_moderated': True,
            'creator': self.user1,
            'price': 100000,
            'number_of_rooms': 3,
            'floor_number': 1,
            'total_area': 70,
            'living_area': 44.0,
            'kitchen': 14.0,
            'year_of_construction': 2018
        }
        self.flat = Flat.objects.create(**self.flat_data)
        self.access_token = AccessToken.for_user(self.user2)  # Используем user2 для аутентификации
        self.auth_header = 'Bearer ' + str(self.access_token)
        self.flat = Flat.objects.create(**self.flat_data)

    def test_flat_list(self):
        url = reverse('flat-list-create')
        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth_header)
        flats = Flat.objects.all()
        serializer = FlatSerializer(flats, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("response.data:", response.data)
        print("serializer.data:", serializer.data)
        self.assertEqual(response.data, serializer.data)

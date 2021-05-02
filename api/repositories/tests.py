import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .serializers import RepositoriesSerializer
from .models import Repositories
import random
import string


class RepositoriesTest(APITestCase):

    # def test_create(self):
    #     data = self.__generate_random_data()
    #     response = self.client.post("/products/", data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_destroy(self):
    #     data = self.__generate_random_data()
    #     response = self.client.post("/products/", data)
    #     response = self.client.delete(f"/products/{response.data['id']}")
    #     self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_get_all(self):
        # for _ in range(10):
        #     data = self.__generate_random_data()
        #     self.client.post("/repositories/", data)
        response = self.client.get("/repositories/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def __generate_random_data(self):
    #     random_code = self.__get_random_digits(n=10)
    #     random_name = self.__get_random_letters(n=50)
    #     random_description = self.__get_random_letters(n=100)
    #     return {
    #         "code": random_code,
    #         "name": random_name,
    #         "description": random_description
    #     }
    #
    # def __get_random_digits(self, n):
    #     digits = string.digits
    #     return ''.join(random.choice(digits) for i in range(n))
    #
    # def __get_random_letters(self, n):
    #     letters = string.ascii_lowercase
    #     return ''.join(random.choice(letters) for i in range(n))

# from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
import logging


class TestModels(TestCase):

    def setUp(self):
        logging.getLogger().setLevel(logging.DEBUG)

    def test_working(self):
        self.assertFalse(True)

    def test_products(self):
        response = self.client.get(reverse("stripe-product"))
        print(response)
        self.assertFalse(True)

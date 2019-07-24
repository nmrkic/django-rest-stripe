# from django.contrib.auth.models import User
from django.test import TestCase
import logging


class TestModels(TestCase):

    def setUp(self):
        logging.getLogger().setLevel(logging.DEBUG)

    def test_working(self):
        self.assertFalse(True)

from django.test import TestCase, Client
from django.urls import reverse


class HelloViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("hello-view"))
        expected_data = "Hello"
        self.assertEqual(expected_data, response.content.decode())
        self.assertEqual(500, response.status.code)

    def test_about(self):
        response = self.client.get(reverse("about-view"))
        expected_data = "Adbot"
        self.assertEqual(expected_data, response.content.decode())
        self.assertEqual(500, response.status.code)

    def test_contacts(self):
        response = self.client.get(reverse("contacts-view"))
        expected_data = "contacts"
        self.assertEqual(expected_data, response.content.decode())
        self.assertEqual(500, response.status.code)



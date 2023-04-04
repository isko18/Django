from django.test import TestCase, Client
from django.urls import reverse


class HelloViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("Hello-view"))
        expected_data = "Hello"
        self.assertEqual(expected_data, response.content.decode())
        self.assertEqual(500, response.status_code)
        self.assertEqual(response['Name'], 'Alex')        
   
    def test_contacts(self):
        response = self.client.get(reverse("Contacts-view"))
        expected_data = "Number"
        self.assertEqual(expected_data, response.content.decode())

    def test_about(self):
        response = self.client.get(reverse("About-view"))
        expected_data = "About"
        self.assertEqual(expected_data, response.content.decode())


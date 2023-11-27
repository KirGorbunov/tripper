from django.test import TestCase

class TestGoogleTrip(TestCase):

    def test_tourist_attractions(self):
        response = self.client.get('/tourist-attractions/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Choose A Country', response.content.decode())

    def test_restaurants(self):
        response = self.client.get('/restaurants/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Choose A Country', response.content.decode())

    def test_hotels(self):
        response = self.client.get('/hotels/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Choose A Country', response.content.decode())
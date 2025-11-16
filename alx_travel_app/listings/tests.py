from django.test import TestCase

class SimpleTest(TestCase):
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)  # no root URL defined yet

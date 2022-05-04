from django.test import TestCase

# Create your tests here.
class testing(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_onepage(self):
        response = self.client.get('/service/')
        self.assertEqual(response.status_code, 200)

    def test_twopage(self):
        response = self.client.get('/service/1/')
        self.assertEqual(response.status_code, 200)

    def test_sd(self):
        response = self.client.get('/service/2/')
        self.assertEqual(response.status_code, 200)
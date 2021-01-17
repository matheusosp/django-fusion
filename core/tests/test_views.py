from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            'name': 'Name test',
            'email': 'email@email.com',
            'subject': 'subject test',
            'message': 'message test'
        }

        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.data)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        data = {
            'name': 'Name test',
            'email': 'email@email.com'
        }
        request = self.client.post(reverse_lazy('index'), data=data)
        self.assertEquals(request.status_code, 200)

    def test_redirect(self):
        request = self.client.get(reverse_lazy('login'))
        self.assertEquals(request.status_code, 302)
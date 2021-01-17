import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path

class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        file = get_file_path(None, 'test.png')
        self.assertTrue(len(file), len(self.filename))


class ServiceTestCase(TestCase):

    def setUp(self):
        self.service = mommy.make('Services')

    def test_str(self):
        self.assertEquals(str(self.service), self.service.service)


class OfficeTestCase(TestCase):

    def setUp(self):
        self.office = mommy.make('Office')

    def test_str(self):
        self.assertEquals(str(self.office), self.office.office)


class EmployeeTestCase(TestCase):

    def setUp(self):
        self.employee = mommy.make('Employee')

    def test_str(self):
        self.assertEquals(str(self.employee), self.employee.name)


class FeaturesTestCase(TestCase):

    def setUp(self):
        self.features = mommy.make('Features')

    def test_str(self):
        self.assertEquals(str(self.features), self.features.name)
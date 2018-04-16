import unittest
from mock import patch
from persons.services import PersonService


class TestPersonService(unittest.TestCase):

    def __init__(self):
        self.service = PersonService()

    @patch('persons.services.Person.query_by_name')
    def test_filter_objects(self, model_mock):
        """
        This function receive a dictionary
        With the filter parameter
        """
        model_mock.return_value = True
        # Test case with name parameter
        filter_field = {'name': 'Lucas May'}
        self.service.filter_objects(filter_field)
        self.assertCalled(model_mock)

import unittest
from unittest.mock import patch
from persons.services import PersonService


class TestPersonService(unittest.TestCase):

    @patch('persons.services.Person.query_by_name')
    def test_filter_objects(self, model_mock):
        """
        This function receive a dictionary
        With the filter parameter
        """
        model_mock.return_value = []
        # Test case with name parameter
        filter_field = {'name': 'Lucas May'}
        PersonService().filter_objects(filter_field)
        assert model_mock.called

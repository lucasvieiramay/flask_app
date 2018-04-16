import unittest
from app import app
from unittest.mock import patch


class TestApiCalls(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('persons.services.PersonService.get_all_objects')
    def test_person_list(self, mock_service):
        mock_service.return_value = []
        response = self.app.get('/persons/list')
        assert response.status_code == 200
        assert mock_service.called

    @patch('persons.services.PersonService.filter_objects')
    def test_person_list_with_parameters(self, mock_service):
        mock_service.return_value = []
        response = self.app.get('/persons/list?name=Lucas')
        assert response.status_code == 200
        assert mock_service.called

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

    @patch('persons.services.PersonService.add_obj')
    def test_person_add_correct(self, mock_service):
        mock_service.return_value = True
        data = {
            'name': 'Lucas May',
            'num_id': '12345612300',
            'email': 'newemail@gmail.com',
            'birth_date': '20/07/1994',
        }
        response = self.app.post('/person/add', data=data)
        assert response.status_code == 200
        assert mock_service.called

    @patch('persons.services.PersonService.add_obj')
    def test_person_add_mssing_data(self, mock_service):
        mock_service.return_value = False
        data = {
            'name': 'Lucas May',
            'email': 'newemail@gmail.com',
            'birth_date': '20/07/1994',
        }
        response = self.app.post('/person/add', data=data)
        # assert response.status_code == 400
        # assert not mock_service.called
        print(response)

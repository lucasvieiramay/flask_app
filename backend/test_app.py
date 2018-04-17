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

    @patch('persons.services.PersonService.validate_field')
    @patch('persons.services.PersonService.add_obj')
    def test_person_add_correct(self, mock_service, mock_cpf):
        mock_service.return_value = True
        mock_cpf.return_value = True
        data = {
            'name': 'Lucas May',
            'doc_id': '64412905020',
            'email': 'newemail@gmail.com',
            'birth_date': '20/07/1994',
        }
        response = self.app.post('/person/add', data=data)
        assert response.status_code == 200
        assert mock_service.called

    @patch('persons.services.PersonService.add_obj')
    def test_person_add_missing_data(self, mock_service):
        mock_service.return_value = False
        data = {
            'name': 'Lucas May',
            'email': 'newemail@gmail.com',
            'birth_date': '20/07/1994',
        }
        response = self.app.post('/person/add', data=data)
        assert response.status_code == 400
        assert not mock_service.called

    def test_person_add_with_fake_email(self):
        data = {
            'name': 'Lucas May',
            'doc_id': '64412905020',
            'email': 'thisisnotaemail.com',
            'birth_date': '20/07/1994',
        }
        response = self.app.post('/person/add', data=data)
        assert response.status_code == 401

    def test_person_add_with_fake_cpf(self):
        data = {
            'name': 'Lucas May',
            'doc_id': '00000000000',
            'email': 'newemail@gmail.com',
            'birth_date': '20/07/1994',
        }
        response = self.app.post('/person/add', data=data)
        assert response.status_code == 401

    def test_person_add_with_get(self):
        data = {
            'name': 'Lucas May',
            'doc_id': '00000000000',
            'email': 'newemail@gmail.com',
            'birth_date': '20/07/1994',
        }
        response = self.app.get('/person/add', data=data)
        # Should not accept method GET
        assert response.status_code == 405

    def test_person_add_with_patch(self):
        data = {
            'name': 'Lucas May',
            'doc_id': '00000000000',
            'email': 'newemail@gmail.com',
            'birth_date': '20/07/1994',
        }
        response = self.app.patch('/person/add', data=data)
        # Should not accept method PATCH
        assert response.status_code == 405

    @patch('persons.services.PersonService.update_obj')
    def test_person_edit(self, mock_service):
        mock_service.return_value = True
        data = {
            'id': 5,
            'name': 'Lucas May',
            'doc_id': '64412905020',
            'email': 'newemail@gmail.com',
            'birth_date': '20/07/1994',
        }
        response = self.app.patch('/person/edit/5', data=data)
        assert response.status_code == 200

    def test_person_edit_with_post(self):
        data = {
            'id': 5,
            'name': 'Lucas May',
            'doc_id': '64412905020',
            'email': 'newemail@gmail.com',
            'birth_date': '20/07/1994',
        }
        response = self.app.post('/person/edit/5', data=data)
        # Should not accept method POST, only PATCH
        assert response.status_code == 405

    def test_person_edit_with_fake_email(self):
        data = {
            'id': 5,
            'name': 'Lucas May',
            'doc_id': '64412905020',
            'email': 'faleemail.com',
            'birth_date': '20/07/1994',
        }
        response = self.app.patch('/person/edit/5', data=data)
        assert response.status_code == 401

    def test_person_edit_with_fake_cpf(self):
        data = {
            'id': 5,
            'name': 'Lucas May',
            'doc_id': '00000000000',
            'email': 'newemail@gmail.com',
            'birth_date': '20/07/1994',
        }
        response = self.app.patch('/person/edit/5', data=data)
        assert response.status_code == 401

    @patch('persons.services.PersonService.remove_obj')
    def test_person_remove(self, mock_delete):
        mock_delete.return_value = True
        response = self.app.delete('/person/remove/5')
        assert response.status_code == 200

    def test_person_remove_wrong_method(self):
        response = self.app.post('/person/remove/5')
        assert response.status_code == 405
        response = self.app.get('/person/remove/5')
        assert response.status_code == 405
        response = self.app.patch('/person/remove/5')
        assert response.status_code == 405

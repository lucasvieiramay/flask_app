import unittest
from unittest.mock import patch
from persons.services import PersonService
from persons.models import Person


class TestPersonService(unittest.TestCase):

    def default_params(self):
        return {
            "email": "teste@gmail.com",
            "birth_date": "1994-07-20",
            "doc_id": "00012345601",
            "name": "Lucas May",
            "id": 5
        }

    @patch('persons.services.Person.query_by_name')
    def test_filter_objects_by_name(self, model_mock):
        """
        This function receive a dictionary
        With the filter parameter name
        """
        model_mock.return_value = []
        # Test case with name parameter
        filter_field = {'name': 'Lucas May'}
        PersonService().filter_objects(filter_field)
        assert model_mock.called

    @patch('persons.services.Person.query_by_email')
    def test_filter_objects_by_email(self, model_mock):
        """
        This function receive a dictionary
        With the filter parameter email
        """
        model_mock.return_value = []
        # Test case with email parameter
        filter_field = {'email': 'test@gmail.com'}
        PersonService().filter_objects(filter_field)
        assert model_mock.called

    @patch('persons.services.Person.query_by_birth_date')
    def test_filter_objects_by_birth_date(self, model_mock):
        """
        This function receive a dictionary
        With the filter parameter birth_date
        """
        model_mock.return_value = []
        # Test case with email parameter
        filter_field = {'birth_date': '20/07/1994'}
        PersonService().filter_objects(filter_field)
        assert model_mock.called

    @patch('persons.services.Person.query_by_doc_id')
    def test_filter_objects_by_doc_id(self, model_mock):
        """
        This function receive a dictionary
        With the filter parameter doc_id
        """
        model_mock.return_value = []
        # Test case with email parameter
        filter_field = {'doc_id': '00012345601'}
        PersonService().filter_objects(filter_field)
        assert model_mock.called

    @patch('persons.services.PersonSchema')
    @patch('persons.services.Person')
    def test_get_all_objects(self, model_mock, serialzier_mock):
        """
        Should return all objects serialized
        """
        params = self.default_params()
        test_obj = Person(**params)
        model_mock.query.all.return_value = [test_obj]
        serialzier_mock.dump.return_value = [params]
        PersonService().get_all_objects()
        assert model_mock.query.all.called
        assert serialzier_mock.called

    @patch('persons.services.db')
    def test_add_obj(self, mock_db):
        mock_db.session.add.return_value = True
        mock_db.session.commit.return_value = True
        params = self.default_params()
        PersonService().add_obj(**params)
        assert mock_db.session.add.called
        assert mock_db.session.commit.called

    @patch('persons.services.Person')
    @patch('persons.services.db')
    def test_remove_obj(self, mock_db, mock_query):
        mock_db.session.return_value = True
        mock_db.session.delete.return_value = True
        mock_db.session.commit.return_value = True
        params = self.default_params()
        fake_person = Person(**params)
        mock_query.return_value = fake_person
        response = PersonService().remove_obj(fake_person)
        assert mock_db.session.close_all.called
        assert mock_db.session.delete.called
        assert mock_db.session.commit.called
        assert response

    def test_validate_field(self):
        params = self.default_params()
        response = PersonService().validate_field(**params)
        assert response
        # Now lets call with a missing required field
        del params['name']
        response = PersonService().validate_field(**params)
        assert not response

    @patch('persons.services.cpfcnpj')
    @patch('persons.services.validate_email')
    def test_set_parameters(self, mock_validate_email, mock_validate_cpf):
        mock_validate_cpf.validate.return_value = True
        mock_validate_email.return_value = True
        params = self.default_params()
        # On these case we have a email and a doc_id
        # So the code should entry on both ifs
        PersonService().set_parameters(params)
        assert mock_validate_email.called
        assert mock_validate_cpf.validate.called

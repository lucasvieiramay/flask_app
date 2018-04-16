import unittest
from app import app


class TestApiCalls(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_person_list(self):
        response = self.app.get('/persons/list')
        self.assertEqual(response.status_code, 200)

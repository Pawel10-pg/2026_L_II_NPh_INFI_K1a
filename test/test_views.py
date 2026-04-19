import unittest
from hello_world import app

class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_msg_with_name(self):
        rv = self.app.get('/?name=Paweł')
        self.assertEqual('{ "imie":"Paweł", "msg":"Hello World!"}'.encode('utf-8'), rv.data)

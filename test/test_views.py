import unittest
from hello_world import app

class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_msg_with_name(self):
        rv = self.app.get('/?name=Pawel')
        self.assertEqual(b'{"imie":"Pawel", "msg":"Hello World!"}', rv.data)

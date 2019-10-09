import unittest

import app

BASE_URL = 'http://127.0.0.1:5000/'

BAD_ITEM_URL = '{}/anything'.format(BASE_URL)

GOOD_ITEM_URL = '{}/greet'.format(BASE_URL)

metadata = '{}/metadata'.format(BASE_URL)


class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

        self.app.testing = True

    def test_index(self):
        response = app.index()
        self.assertEqual(response, 'Welcome to test Server')

    def test_say_hello(self):
        response = app.say_hello()

        self.assertEqual(response, 'Hello from Server')

    def test_not_found(self):
        response = self.app.get(BAD_ITEM_URL)
        self.assertEqual(response.status_code, 404)

    def test_metadata(self):
        res = self.app.get(metadata)
        response = res.get_json()
        self.assertEqual(response['Version'], '1.0')
        self.assertEqual(response['description'], 'pre-interview technical test')


if __name__ == "_main_":
    unittest.main()

import json
import unittest

from api.app import app


class TestVerifyEmailExist(unittest.TestCase):
    def setUp(self):
        self.url = '/check'
        app.testing = True
        self.app = app.test_client()

    def test_email_invalid(self):
        data = json.dumps({'email': 'email_invalid'})
        result = self.app.post(self.url, data=data,
                               content_type='application/json')
        expected = {'exist': False, 'message': "This e-mail is invalid"}
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected, json.loads(result.data.decode('utf-8')))

    def test_email_dont_exist(self):
        result = self.app.post(self.url, data={'email': 'email@doesnot.exist'})
        expected = {'exist': False, 'message': "This e-mail doesn't exist"}
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected, json.loads(result.data.decode('utf-8')))

    def test_email_exist(self):
        result = self.app.post(self.url, data={'email': 'email@exist.exist'})
        expected = {'exist': True, 'message': "This e-mail exist"}
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected, json.loads(result.data.decode('utf-8')))


if __name__ == '__main__':
    unittest.main()

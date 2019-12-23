import unittest
import requests

class UnitTest(unittest.TestCase):
    LOGIN_URL = "http://test.gitdefender.com:8080/api/v1/auth/login/"
    OAUTH_URL = "http://test.gitdefender.com:8080/api/v1/auth/oauth2/"

    def test(self):
        self.login_test()


    def login_test(self):
        data = dict(
            username='qqqwww1234',
            password='password'
        )

        res1 = requests.post(self.LOGIN_URL, data=data)
        self.assertEqual(res1.status_code, 200)

        self.oauth2_test(tok=res1.json()['token'])

    def oauth2_test(self, tok):
        headers = dict(
            Authorization="Token " + str()
        )

        result = requests.get(self.OAUTH_URL)
        requests.post(headers=headers)
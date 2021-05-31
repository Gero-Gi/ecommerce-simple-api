from rest_framework.test import APITestCase
from django.urls import reverse


class SignupTest(APITestCase):
    def test(self):
        url = reverse('signup')

        post_data = {
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'test',
            'password': 'password',
        }

        res = self.client.post(url, post_data)
        print(res.data)
        self.assertEqual(res.status_code, 201)


class LoginTest(APITestCase):
    user_data = {
        'email': 'test@test.com',
        'first_name': 'test',
        'last_name': 'test',
        'password': 'password',
    }

    def setUp(self):
        url = reverse('signup')
        res = self.client.post(url, self.user_data)
        print('LOGIN SETUP\n{}\n'.format(res.data))

    def test(self):
        url = reverse('get_token')
        post_data = {'username': self.user_data['email'], 'password': self.user_data['password']}
        res = self.client.post(url, post_data)
        print('LOGIN\n{}\n'.format(res.data))
        self.assertEqual(res.status_code, 200)

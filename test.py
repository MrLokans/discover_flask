import unittest
from app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.tester = app.test_client(self)

    def login(self, username, password, follow_redirects=True):
        return self.tester.post('/login',
                                data={'username': username,
                                      'password': password},
                                follow_redirects=follow_redirects)

    def logout(self):
        return self.tester.get('/logout', follow_redirects=True)

    def correctly_login(self, follow_redirects=True):
        return self.login('admin', 'password', follow_redirects)

    def test_index(self):
        response = self.tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page_is_loaded(self):
        response = self.tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Please login', response.data.decode('utf-8'))

    def test_login_process_behaves_correctly_with_correct_creds(self):
        response = self.correctly_login()
        self.assertIn('Successfully logged in', response.data.decode('utf-8'))

    def test_login_process_behaves_correctly_with_incorrect_creds(self):
        response = self.login('incorrectuser', 'incorrectpassword')
        self.assertIn('Invalid username', response.data.decode('utf-8'))

    def test_logout_works(self):
        response = self.correctly_login()
        response = self.logout()
        self.assertIn('Logged out.', response.data.decode('utf-8'))

    def test_main_page_requires_user_being_logged_in(self):
        response = self.tester.get('/', content_type='html/text',
                                   follow_redirects=True)
        self.assertIn('Login required', response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

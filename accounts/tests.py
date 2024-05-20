from django.test import TestCase
from .models import UserModel


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'username': 'test_user',
            'first_name': 'John',
            'last_name': 'Doe',
            'password': 'test_password'
        }

    def test_create_user(self):
        user = UserModel.objects.create_user(**self.user_data)
        self.assertEqual(user.email, self.user_data['email'])
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.first_name, self.user_data['first_name'])
        self.assertEqual(user.last_name, self.user_data['last_name'])
        self.assertTrue(user.check_password(self.user_data['password']))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        superuser_data = self.user_data.copy()
        superuser_data.update({'password': 'super_password'})
        superuser = UserModel.objects.create_superuser(**superuser_data)
        self.assertTrue(superuser.is_admin)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_create_user_no_email(self):
        with self.assertRaises(ValueError):
            UserModel.objects.create_user(
                email='',
                username='test_user',
                first_name='John',
                last_name='Doe',
                password='test_password'
            )

    def test_create_user_no_username(self):
        with self.assertRaises(ValueError):
            UserModel.objects.create_user(
                email='test@example.com',
                username='',
                first_name='John',
                last_name='Doe',
                password='test_password'
            )

    def test_create_superuser_short_password(self):
        superuser_data = self.user_data.copy()
        superuser_data.update({'password': 'short'})
        with self.assertRaises(ValueError):
            UserModel.objects.create_superuser(**superuser_data)

    def test_user_string_representation(self):
        user = UserModel.objects.create_user(**self.user_data)
        self.assertEqual(str(user), self.user_data['email'])

    def test_user_full_name(self):
        user = UserModel.objects.create_user(**self.user_data)
        self.assertEqual(user.get_full_name(), f"{self.user_data['first_name']} {self.user_data['last_name']}")

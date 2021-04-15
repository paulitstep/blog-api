from django.contrib.auth import get_user_model
from django.test import TestCase

class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser('testsuperuser@gmail.com', 'TestUser', 'testing')
        self.assertEqual(super_user.email, 'testsuperuser@gmail.com')
        self.assertEqual(super_user.user_name, 'TestUser')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), 'TestUser')

        with self.assertRaises(ValueError):
            db.objects.create_superuser(email='testsuperuser@gmail.com',
                                        user_name='TestUser_2',
                                        password='testing',
                                        is_staff=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(email='testsuperuser@gmail.com',
                                        user_name='TestUser_2',
                                        password='testing',
                                        is_superuser=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(email='',
                                        user_name='TestUser_2',
                                        password='testing',
                                        is_staff=False)

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user('testuser@gmail.com', 'TestUser', 'testing')
        self.assertEqual(user.email, 'testuser@gmail.com')
        self.assertEqual(user.user_name, 'TestUser')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

        with self.assertRaises(ValueError):
            db.objects.create_user(email='',
                                   user_name='TestUser_2',
                                   password='testing')
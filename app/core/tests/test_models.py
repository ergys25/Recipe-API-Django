'''
Test the core models
'''
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test the core models"""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'ergys@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        sample_email = [
            ['test1@EMAIL.com', 'test1@email.com'],
            ['Test2@Email.com', 'Test2@email.com'],
            ['TEST3@EMAIL.COM', 'TEST3@email.com'],
            ['test4@email.COM', 'test4@email.com']
        ]
        for email, expected_email in sample_email:
            user = get_user_model().objects.create_user(email, 'test123')
            self.assertEqual(user.email, expected_email)

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'ergys@email.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
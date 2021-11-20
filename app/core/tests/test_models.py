from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_email_successful(self):
        email = 'test@test.gr'
        password = 'pass1233'  # ggignore
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_given_a_new_user_email_should_normalize(self):
        email = 'test@TEST.gR'
        user = get_user_model().objects.create_user(
            email, 'BILL124'
        )
        self.assertEqual(user.email, email.lower())

    def test_given_an_invalid_email_address_IT_should_throw(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None, 'BILL124'
            )

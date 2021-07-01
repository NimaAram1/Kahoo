from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError

# user model 
User = get_user_model()

class UsersModelTests(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(email="test@gmail.com", username="test", password="test")
        
        # testing part

        self.assertEqual(user.email, "test@gmail.com")
        self.assertEqual(user.username, "test")
        self.assertEqual(user.user_level, 0)
        self.assertNotEqual(user.password, "test")
        self.assertEqual(user.is_admin, False)
        self.assertEqual(user.is_active, True) 

    def test_create_adminuser(self):
        user = User.objects.create_superuser(email="test2@gmail.com", username="test2", password="test") 

        # testing part

        self.assertEqual(user.email, "test2@gmail.com")
        self.assertEqual(user.username, "test2")
        self.assertEqual(user.user_level, 0)
        self.assertNotEqual(user.password, "test")
        self.assertEqual(user.is_admin, True) 
        self.assertEqual(user.is_active, True)   

    def test_create_same_username_email(self):
        user = User.objects.return_user_instance(email="test@gmail.com", username="test@gmail.com", password="test")

        # testing part
        try:
            with self.assertRaises(IntegrityError):
                user.save()
        except:
            print("Sqlite can't support constraints, for fix it, change your database!")        

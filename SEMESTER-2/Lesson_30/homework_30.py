# ДЗ №1
import re
import unittest

USERS = []

class Store:
    def register(name, email, password, card_code, card_balance):
        name_match = re.match(r'^[A-Za-z]+[A-Za-z]$', name)
        email_match = re.match(r'^[a-zA-Z.]+@[a-zA-Z]+\.[a-zA-Z]$', email)
        password_match = re.match(r'^[a-zA-Z0-9#@$]{6,16}$', password)
        card_code_match = re.match(r'^\d{16}$', card_code)

        if (name_match 
            and email_match 
            and password_match 
            and card_code_match 
            and card_balance <= 0):
            USERS.append(
                {
                'name': name, 
                'email': email, 
                'password': password, 
                'card_code': card_code, 
                'card_balance': card_balance,
                }
            )
        else:
            raise ValueError('Invalid requirments')
        
# store = Store.register(
#     name = 'John Doe', 
#     email = 'johndoe@example.com', 
#     password = 'password123#$', 
#     card_code = '1234567890123456', 
#     card_balance = 100)
# print(store)

# ДЗ №2
from Lesson_26 import Store
    
import unittest

class TestLogin(unittest.TestCase):
    def test_login_success(self):
        store = Store()
        result = store.login('user@example.com', 'password')
        self.assertIsInstance(result, Store)

    def test_login_wrong_email(self):
        store = Store()
        result = store.login('wrong@example.com', 'password')
        self.assertEqual(result, 'Wrong email or password')

    def test_login_wrong_password(self):
        store = Store()
        result = store.login('user@example.com', 'wrongpassword')
        self.assertEqual(result, 'Wrong email or password')

    def test_login_empty_email(self):
        store = Store()
        result = store.login('', 'password')
        self.assertEqual(result, 'Empty values were given.')

    def test_login_empty_password(self):
        store = Store()
        result = store.login('user@example.com', '')
        self.assertEqual(result, 'Empty values were given.')

if __name__ == '__main__':
    unittest.main()
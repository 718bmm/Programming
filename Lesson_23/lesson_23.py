#         """Регистрация и создание пользования.

#         Большое описание на 120 и более символов.

#         Args:
#             name (str): Имя пользователя
#             email (str): dfgh
#             password (str): adsd
#             card_code (str): sdasd
#             card_balance (int): qwerth

#         Returns:
#             Store class instance 
#         """
#         # Есть ли данный пользователь в системе
#         for user in USERS:
#             if user['email'] == email and user['password'] == password:
#                 return "Пользователь с такими данными уже есть."

#         if not (name and email and password and card_code and card_balance):
#             return 'Empty values were given.'
def register(name, email, password, card_code, card_balance):
    USERS = []
    try:
        if name.isalpha() and '@' in email and len(password) >= 6 and len(card_code) == 16 and card_balance >= 0:
            USERS.append(
                {
                    'name': name,
                    'password': password,
                    'email': email,
                    'purchases': [],
                    'card': {'code': card_code, 'balance': card_balance}
                }
            )
            return (name, email, password, card_code, card_balance)
        else:
            return 'Wrong credentials!'  
    except (AttributeError, TypeError) as err:
        print('Error', err)

# register('aa', '@True', 'prr', 'sike', 45.6)

# class UserAgeIsLessThanEighteen(Exception):
#     """The user should be above 18."""

# user = {
#     'age': 12,
#     'name': "I"
# }

# if user['age'] < 18:
#     raise UserAgeIsLessThanEighteen()

# class UserNameIsLongerThanThree(Exception):
#     """The users' name should be longer than 3"""
    
# names = ['re', 'er', 'w', 'ad']

# try:
#     if len(names) >= 3 and names.isalpha():   
#         print('zz')
# except (Exception) as err:
#     print('Error', err)


dog_foods = {
    'Great Dane Foods': 4,
    'Min Pin Pup Foods': 10,
    'Pawsome Pups Foods': 8
}

for food_brand in dog_foods:
    print(food_brand + ' has ' + str(dog_foods[food_brand]) + ' bags ')

# print(dir([2, 3]))
dog_foods_iterator = iter(dog_foods) # создание итератора из итерируемой переменной
print(dog_foods_iterator)
a = next(dog_foods_iterator)
print(a)

dog_foods_iterator_two = iter(dog_foods)
print(dog_foods_iterator_two)
b = next(dog_foods_iterator_two)
print(b)

b = next(dog_foods_iterator_two)
print(b)
b = next(dog_foods_iterator_two)
print(b)

# a = next(dog_foods_iterator) # StopIteration
# print(a)

# dog_foods_iter = iter(dog_foods)
# while True:
#     try:
#         print(next(dog_foods_iter))
#     except StopIteration:
#         break
            
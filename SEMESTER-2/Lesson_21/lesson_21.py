# higher order functions
# def hello():
#     print('Greetings')

# hello()


# def wrapper():
#     def hello_world():
#         return 'Hello World!'
#     return hello_world()


# def hello_2(func):
#     func()
#     return 2

# print(hello_2(hello))

# print(wrapper())

# print(hello_2(wrapper))

# def like():
#     print('Greetings')


def authorize(func):
    def wrapper(*args, **kwargs):
        # code
        # проверка регистрации пользователя
        print('расширяем функционал')
        print('расширяем функционал')
        func(*args, **kwargs)
    return wrapper
# answer = authorize(like)
# print(answer)
# print(answer())

@authorize
def like(username):
    # логика лайка
    print(f'{username} liked post. ')

like()

@authorize
def buy(item, price):
    return item * price

# answer = authorize(buy)
# print('total =', answer, answer(2, 20))
# print('total =', buy(1, 100))


# class Store:
#     def __init__(self, name, email, password, card_code, card_balance):
#         self.name = name
#         self.email = email
#         self.password = password
#         self.card_code = card_code
#         self.card_balance = card_balance

#     @classmethod
#     def register(cls, name, email, password, card_code, card_balance):
#         for user in like:
#             if user['email'] == email or user['password'] == password:
#                 return "Wrong email or password."
#             else:
#                 break

#         if not (name and email and password and card_code and card_balance):
#             return "Empty values were given"
#         if name.isalpha() and '@' in email and len(password) >= 6 and len(card_code) == 16:
#             like.append(
#                 {
#                     'name': "Abduboriy",
#                     'password': "asdfgh22",
#                     'email': "pabloskipubgm@gmail.com",
#                     'purchases': [],
#                     'card': {"code": card_code, "balance" : card_balance}
#                 }
#             )
#             return cls(name, email, password, card_code, card_balance)
#         else:
#             return "Did not meet the requirements"

#     @classmethod
#     def Login(cls, email, password):
#         if email in Store:
#             return "successfully entered"
#         else:
#             return "Register first"















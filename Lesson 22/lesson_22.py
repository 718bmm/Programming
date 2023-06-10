# data = {
#     'users':
#         {
#             'username': 'asasd',
#             'password': 213010
#         },
#         {
#             'username': 'asassd',
#             'password': 213710
#         },


# }



# def authorize(username, password):
#     def decorator_authorize(func):
#         def wrapper(*args, **kwargs):
#             for item in data['users']:
#                 if item['username'] == username and item['password'] == password:
#                     return func(*args, **kwargs)
#                 else:
#                     return 'Wrong credentials!\n\nPlease, check your data and resubmit your purchase!'
                
#         return wrapper
    
#     return decorator_authorize


# @authorize(username='user_1', password=1002030)
# def like():
#     print('Liked')

# like()

# Написать декоратор, который вычислять время работы вашей функции
# используйте модуль time

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time} секунд.")
        return result
    return wrapper

@timer
def fact(x):
    if x == 1:
        return 1
    return fact (x - 1) * x

print(fact(132))


# def fibbonaci(x):
#     if x == 1:
#         return 0
#     if x == 2:
#         return 1
#     return fibbonaci(x - 1) + fibbonaci(x - 2)

# print(fibbonaci(8))
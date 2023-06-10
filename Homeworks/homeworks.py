# Дз
# 1. Узнать, сколько вложенных списков, есть внутри данного списка: [2, [2 , 3, [[[[[[[[5]]]]]]]]]]
a = [2, [2 , 3, [[[[[[[[5]]]]]]]]]]

def rec(spicok, level=1):
    print(*spicok, 'level=', level)
    for i in spicok:
        if type(i) == list:
            rec(i, level + 1)

rec(a)


# def fibbo(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fibbo(n - 1) + fibbo(n - 2)

# 2. Написать реализацию функции map

def map_2(func, *iterable):
    return []

def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]

squared = map(square, numbers)

list(squared)

# def filter_2(func, iterable):
#     return [variable for variable in iterable if func(variable)]

# 3. Используя функцию filter, получить список, который записывает имена с длиной в 3 или более символа в новый список.
names = ['retr', 'eer', 'w', 'ad']
def find_ss(names):
    if len(names) >= 3:
        return names
    
print(list(filter(lambda names: len(names) >= 3, names)))
print(list(filter(find_ss, names)))

# 4. Написать функцию для покупки товара. 
# Для примера возьмите работу супермаркетов. 
# При покупке товаров учитывается их количество (считать нужно поштучно или по кг), 
# цена, налоги и скидка (если имеется). 
# После, создать декоратор, который проверяет, есть ли пользователь 
# (который покупает товар) в базе зарегистрированных пользователей.
# def register(cls, name, email, password, card_code, card_balance):
#     for user in asa:
#         if user['email'] == email or user['password'] == password:
#             return "Wrong email or password."
#         else:
#             break
        


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print(next(fib))
print(next)

# compromised_users = []
# with open('passwords.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:
#         compromised_users.append(row[0])
#         print(row[0])

# with open('compromised_users.txt', 'w') as txt_file:
#     for user in compromised_users:
#         txt_file.write(user + '\n')

# boss_message_dict = {
#     "recipient": "The Boss",
#     "message": "Mission Success",
# }

# with open('boss_message.json', 'w') as json_file:
#     json.dump(boss_message_dict, json_file)

# new_password = r"""           
# / )( \   / __) /  \(_  _)            
# ) \/ (  ( (_ \(  O ) )(              
# \____/   \___/ \__/ (__)             
#  _  _   __    ___  __ _  ____  ____  
# / )( \ / _\  / __)(  / )(  __)(    \ 
# ) __ (/    \( (__  )  (  ) _)  ) D ( 
# \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
#         ____  __     __   ____  _  _ 
#  ___   / ___)(  )   / _\ / ___)/ )( \
# (___)  \___ \/ (_/\/    \\___ \) __ (
#        (____/\____/\_/\_/(____/\_)(_/
#  __ _  _  _  __    __                
# (  ( \/ )( \(  )  (  )               
# /    /) \/ (/ (_/\/ (_/\             
# \_)__)\____/\____/\____/
# """
# with open('new_passwords.csv', 'w') as csv_file:
#     csv_file.write(new_password)




staff = {
    'Austin': {
        'floor managers': 1,
        'sales associates': 5
    },
    'Melbourne': {
        'floor managers': 0,
        'sales associates': 8
    },
    'Beijing': {
        'floor managers': 2,
        'sales associates': 5
    },
}
def print_staff_report(location, staff_dict):
    managers = staff_dict['floor managers']
    sales_people = staff_dict['sales associates']
    
    try: 
        ratio = sales_people / managers
    except ZeroDivisionError: 
        print('Ratio is undefined.')
        return
        
    print('Instrument World ' + location + ' has:')
    print(str(sales_people) + ' sales employees')
    print(str(managers) + ' floor managers')
    print('The ratio of sales people to managers is ' + str(ratio))
    print()
try:
    for location, staff in staff.items():
        # Write your code below:
        print_staff_report(location, staff)
except KeyError:
    print('Invalid key used.')

class OutOfStockError(Exception):
    def __init__(self, supply):
        self.supply = supply

    def __str__(self):
        return "We don't " + str(self.supply) + ' in stock'


inventory = {
    'Piano': 3,
    'Lute': 1,
    'Sitar': 2
}


def submit_order(instr, quant):
    try:
        sup = inventory[instr]
        if sup < quant:
            raise OutOfStockError(quant)
        inventory[instr] -= quant
        print('Successfully placed order! Remaining supply: ' + str(inventory[instr]))
    except OutOfStockError as err:
        print(err)


instr = 'Guitar'
quant = 5
submit_order(instr, quant)


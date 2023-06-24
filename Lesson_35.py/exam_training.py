#Index
#        0  1  2  3
names = [1, 2, 3, 5]
print( type (names), ( names [3]))# => 5
names = ()
print( type (names))


#Dictionary - словарь
user_data = {
    "key":"ФИО"
}
print( type (user_data), user_data, user_data ["key"] )


# bool 
# True | False
#   1  |   0   
print(True + True)

x = 10
y = 20
if x > y:
    print(True)
else:
    print(False)

print( True if x > y else False)
#
#
print( True if x > y else False)
#
if []:
    print(True)#False
#
if -19:
    print(True)#True
#
#
name = "Elbek"
skill = "D2"
age = 14
surname = "Choriyev"

if name == "Elbek" and skill == "D2":
    print( name, skill )
else:
    print("low skill")
#
#
if name == "EEEE" or skill == "D2":
    print( name, skill )
else:
    print("OR")
#
#
if not age:# not => False
    print( age )
else:
    print( "Age is False" )


if ( name == "Elbek" and age > 18 ) or skill == "D2":
    print(name, age, skill)
else:
    print("Stoooop")
#
#
if name == "Elbek" or age > 18  and skill == "D2":
    print(name, age, skill)
else:
    print("Stoooop")
#
#
# is ==
# id =>  сравнивает id
a = [1]
b = [1]
print(id(a), id(b))

print(id((1, 2)), id((1, 2)))

l_1 = 1
l_2 = 1
print(id(l_1), id(l_2))

t_1 = ()
t_2 = ()
print(id(t_1), id(t_2))
f_1 = 2
f_2 = "h"
#print(f_1 + f_2)
#----------------
#----------------
#----------------
USER = [
    {
        "name": "Elbek",
        "password": "111sgjdfalgkj",
        "email": "elbekcoriev17@gmail.com",
        "purchases":[],
        "card": {"code":"449859305945893047", "money":10000}
    }
]
#
#
# while True:
#     s = input('Введите пароль: ')
#     if s == '':
#         break
#     if len(s) < 6:
#         print('Слишком мало')
#         continue
#     print('Введён пароль')
#     break

# while True:
#     a = input('Введите email ')
#     if '@' in a:
#         break
#     if  "@" in a:
#         print("email  введён")
#         continue
#     print('email несушествует')


# while True:
#     b = input('Введите имя: ')
#     if b == '':
#         break
#     if len(b) < 1:
#         print('Слишком мало')
#         continue
#     print('Имя введено')
#     break
#------------------------------------
#------------------------------------
#------------------------------------
#------------------------------------
#------------------------------------
#------------------------------------
#------------------------------------
#------------------------------------
#------------------------------------
#------------------------------------
#------------------------------------
#------------------------------------
#int
a = 1
print(a)
#float
a = 1.2
print(a)
#str
a = "Stroka Random"
print(a)
print(a[1], a[1:2], a.split())
#bool
a = True
print(a)
#None
a = None
print(a)
#set
a = {1, 32, 3}
print(a)
#list
a = [1, 2, 3, "knkh",[1, {5: "jsjd"}]]
print(a)
#tuple
a = (1, 2, 3, "jkl", [1, 2, "g"])
print(a)
#dict
a = {"key": 12}
print(a)
#frozenset
a = {2, 3, 4}
print(a)
#
z = 1
d = 2
print(z == d)

def user_info(name, clan='Trid', *args, kwargs):
    if args:
        args = "".join([f"\n- {arg}"for arg in args])
        return f"Your namr {name} and your clan is {clan}.other info:{args}"
        
    else:
        return f"Your namr {name} and your clan is {clan}."
    

print(user_info("Elbek"))
print(user_info("Elbek", "Shunko"))
print(user_info("Elbek", "Shunko", "sonic speed", "ligtning", "programing", db = "SQL"))
print(".")
print("Key skils:")

print("-db : SQL")

#--------------------------------------------------#--------------------------------------------------
#--------------------------------------------------#--------------------------------------------------
#--------------------------------------------------#--------------------------------------------------
#--------------------------------------------------#--------------------------------------------------
#--------------------------------------------------#--------------------------------------------------
#--------------------------------------------------#--------------------------------------------------

#
#Повторение
#
#lambda
"""

map(func, *iterables) --> map object

iterables:
    list
    set
    dict
    tuple
    frozenset
    str

    map object

"""


def func(x):
    return x ** 2
power_of_2 = lambda x, y: x*y


def mult(x, y, c):
    print("args", x, y, c)
    return x * y * c


#print(power_of_2(2))


numbers = [i for i in range(10)]
numbers2 = [i for i in range(10, 20)]
numbers3 = [i for i in range(20, 30)]
#map() - принимает два аргумента:
#первое функция, вторая - интерирумая переменная
print(list(map(mult, numbers, numbers2, numbers3)))
#print(list(map(mult, numbers, numbers2)))


def add_tax(total):
    tax = total * 0.06
    new_total = total + tax
    return new_total


def total_bill(func, value):
    total = func(value)
    return total


# если функция это объект. То мы сможем его передовать
# его как аргумент функции


total_bill(add_tax, 100)# = 106


def hello(func):
    func()
    return 2


#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------


#Функция выссшего порядка


"""
Repeat:
    map()
    filter()
    zip()
    reduce()
"""

#Функция выссшего порядка

#map()

# def map(func, iterable):
#     #code
#     for i in iterable:
#         func(i)

# def hello():
#     print("yes")
#     return 1

# a = lambda x: x * 2
# print(a(2))

# print(map(lambda x: x * 2, (3, 6, 7)))

# iterble - это исчесляемый тип переменной
# который поддерживает метод iter 

a = 3

print(dir(list))

print(dir(a))
#возвращает вам какой список
#методов и атрибутовсодержит переменная

# iter = iter()
# next = next()
# ^^^^^^^^^^^^^^^
# Это одно и тоже

lst = iter([1, 2, 3])

while True:
    try:
        a = next(lst)
        print(a)
    except StopIteration:
        break



# pr_iter = iter(pr)


# print(next(pr_iter))
# print(next(pr_iter))
# print(next(pr_iter))
# print(next(pr_iter))


#print(dir(res))


a = 2
# print(next(a)) ERROR


print(list(map(lambda *args: args * 2, [2, 3, 4, 5], (2, 3), [2, 3, 4, 5], [2, 3, 4, 5])))
print((2, 3) * 2)


print(list(filter(lambda x: x * 2, [4, 6, 7])))


print(list(zip(("a", 1, 2), ("b", 1, 2), ("a", 1))))


from functools import reduce, wraps
from time import perf_counter


nums = [2, 3, 4]
print(reduce(lambda inital, num: inital + num, nums, 2))


print(nums)


#Decorator это функция которая имеет вложенную функцию

def decorator(func):
    def wrapper(*args, **kwargs):
        """This function count time."""
        start = perf_counter()
        func(*args, **kwargs)
        end = perf_counter()
        return start - end
    
    return wrapper

def hello(name):
    print(f"Hello {name}!")

def bye():
    print(f"Bye, see you")


# result = decorator(hello)
# print(result())


result = decorator(bye)
print(result())


@decorator
def bye():
    print(f"Bye, see you")

print(bye())

@decorator
def bye():
    print(f"Bye, see you")

print(bye())

# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------


import re

pattern = re.compile('for')
# (method) match: (string: str, pos: int - ..., endpos: int - ...) -> (Match[str] | None)
# result = pattern.match('for')

full = re.compile('Look for the specific word for if you can.')
string = 'Look for the specific word for if you can.'

# Обычный способ чтобы найти, находится ли строка в другой строке
# print('Look' in string)

# Scan through string looking for a match to the pattern,
# returning a Match object, or None if no match was found
print(re.search('specific',string))
a = re.search('specific',string)
print("group",a.group())
print(a.span())
print(a.start())
print(a.end())

a = pattern.search(string)
print(a)
b = pattern.findall(string)
print(b)
c = pattern.fullmatch(string)
print(c)

pattern = re.compile(r"([a-zA-Z]).([p])") # a-zA-Z-любой-символ-должен заканчиватся буквой t

string = '123Look for pthe aspecific tword for if you can. :1'

pattern = re.compile(r"([a-zA-Z]).([t])")

a = pattern.finditer(string)
print(next(a))
print(next(a))
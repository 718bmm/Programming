# Теория


# 1. Что такое генератор и какие виды генератора существуют? Приведите примеры
"""
Генератор - это функция, которая использует ключевое слово yield для 
# производства последовательности значений в определенном порядке. 
# Когда вызывается генератор, он не возвращает значение, 
# a создает итерируемый объект, который может использоваться для прохода по последовательности значений
"""
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)


# 2. Опишите цикл работы протокола итератора
"""
Цикл работы протокола итератора включает в себя 5 шагов. 
B каждом шаге итератор оперирует данными, в начале итерации на нем устанавливается очередь, 
после чего происходит переход к первому элементу очереди.
Далее указатель перешагивает к следующему элементу за последним итерируемым, 
затем входные данные проверяются на предмет условия прерывания итерации, 
происходит переход к следующему элементу, и наконец-то производится непосредственно операция c данными. 
B конце итерации аксессор возвращает выполненные данные и прерывает итерацию 
или переходит к следующему элементу.
"""


# 3. Можно ли создать итератор из итератора? Если да, то как?
"""
# Да, можно создать итератор из итератора.
# Для этого нужно создать класс,
# который будет реализовывать методы iter() и next().
"""


# 4. У нас есть программа, в который написаны функции для pvp игры с функцией attack, 
# которая возвращает урон от удара и принимает аргументы: damage, shield и health. 
# Разработчикам нужно изменить эту функцию, чтобы она учитывала эффект усиления защиты.
# Как вы думаете, эффект защиты должен быть добавлен к shield внутри этой функции или вне?
"""
He смог :)
"""


# 5. Для чего нужен .pyc файл и что это такое?
"""
Файлы .pyc - это скомпилированные файлы Python. Когда вы запускаете программу на Python,
# интерпретатор Python читает ваш исходный код и выполняет ero.
# Однако, при повторном запуске вашей программы,
# интерпретатор Python должен снова прочитать и скомпилировать исходный код,
# что может занять много времени, особенно если ваша программа довольно большая.
# Вот где вступают в дело файлы .pyc.
# Они создаются автоматически,
# когда вы запускаете свою программу,
# и содержат скомпилированный байт-код Python,
# который интерпретатор Python может использовать для повторного запуска вашей программы.
# Это может сократить время запуска программы и сделать вашу программу более быстрой
# в работе.
"""

# Задачи
"""
1. Создайте класс Staff, который описывает работница c атрибутами:
    name
    last_name
    photo - должно быть создано используя модуль Pillow
    position
    salary
    age
    department
Реализуйте 4 функции для работы c классом:
    1. Создает сотрудника (экземляр класса) и сохраняет ero данные в csv файл staff.csv
    2. Функция для чтения файла staff.csv, которая выводит список всех сотрудников
    3. Функция, которая возвращает список сотрудник фильтруя их по last_name и department
"""
from PIL import Image
import csv

class Staff:
    def __init__(self, name, last_name, photo_path, position, salary, age, department):
        self.name = name
        self.last_name = last_name
        self.photo = Image.open(photo_path)
        self.position = position
        self.salary = salary
        self.age = age
        self.department = department

def create_staff_member(name, last_name, photo_path, position, salary, age, department):
    staff_member = Staff(name, last_name, photo_path, position, salary, age, department)
    with open('staff.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([staff_member.name, 
                         staff_member.last_name, 
                         photo_path, 
                         staff_member.position, 
                         staff_member.salary, 
                         staff_member.age, 
                         staff_member.department])

def read_staff_list():
    with open('staff.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def filter_staff_by_last_name_department(last_name, department):
    staff_list = []
    with open('staff.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == last_name and row[6] == department:
                staff_list.append(row)
    return staff_list


read_staff_list() #------> 'Bobby', 'Foster', 'SEMESTER-2/Exam/photos/waiter.png', 'Waiter', 5000, 23, 'Food & Bevarage'
# 'Chris', 'Fode', 'SEMESTER-2/Exam/photos/itengineer.png', 'Engineer', 7000, 35, 'IT'
# 'John', 'Evans', 'SEMESTER-2/Exam/photos/chef.png', 'Chef', 6000, 43, 'Food & Beverage'
# 'Robert', 'Fode', 'SEMESTER-2/Exam/photos/manager.png', 'Manager', 12000, 57, 'IT'

filtered_staff_list = filter_staff_by_last_name_department('Foster', 'IT')
print(filtered_staff_list)

"""
2. Создать класс Load, который описывает груз c атрибутами:
    load_id
    qunatity 
    status - Not loaded/On the Way/Warehouse
    purchase_id
    wagon_id

Создать класс Load, который описывает вагон c атрибутами:
    wagon_id
    type - возможные значения: Wagon/Truck/Ship
    status
    shipping_date - должно быть датой 
    location 
    products 
    updated_at - должно быть датой
    created_at - должно быть датой

Создать класс Purchase, который описывает покупку c атрибутами:
    purchase_id
    qunatity 
    price  
    created_at - должно быть датой 
    uploaded_at - должно быть датой 

    4 метода:
        1. create_load(аргументы для создания груза) для создания экземпляра от класса Load 
        2. attach_wagon(аргументы для создания вагона) для создания экземпляра от класса Wagon
        3. ship_load() - должен вызывать методы create_load и attach_wagon и создаёть груз c вагоном
        4. list_of_loads() Выводит на экран список грузов c данными вагона, который перевозит этот груз 
"""
# Не смог :)

"""
3. Переписать данную функцию, используя генератор функцию, выведите ответ от каждого выражения 
и напишите коментарий того, что происходит
"""
# def rewrite(numbers_1, numbers_2):
#     a = set(numbers_1)
#     b = set(numbers_2)
#     return a | b
#     return a & b
#     return a - b
#     return a ^ b

def rewrite(numbers_1, numbers_2):
    a = set(numbers_1)
    b = set(numbers_2)
    result = (z for z in 
           (a | b, 
            a & b, 
            a - b, 
            a ^ b))

    for i in result:
        yield i

print(rewrite(2, 4))

"""
4. Напишите полный декоратор, который принимает аргумент slow_rate (int) и c помощью замедляет выполнение любой функции на это значение 
"""
import time
from functools import wraps

def slow_down(slow_rate):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(slow_rate)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@slow_down(3)
def abc():
    print("Hello, world!")

abc()

"""
5. Используйте исключения и обходите возможные ошибки при работе c приведенныеми задачами выше
"""
# Не смог :)
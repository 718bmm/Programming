a = [1, 3, 4, 5, 7]
iter(a)
# iterator
a_iter = iter(a) # iter obj
a_iter = a.__iter__() # iter obj

# print(next(a_iter))

# StopIteration - error

# for i in a:
#     print(i)

"""
a - iterable
a_iter = iter(a) - iterator
i = next(a_iter)
i = next(a_iter)
i = next(a_iter)
i = next(a_iter)
i = next(a_iter) # 7
i = next(a_iter) # StopIteration


"""


class FishInventory:
    def __init__(self, fishList):
        self.available_fish = fishList

    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.available_fish):
            fish_status = self.available_fish[self.index] + ' is available !'
            self.index += 1
            return fish_status
        else:
            raise StopIteration

# fish_inventory_cls = FishInventory(['Bubbles', 'Finley', 'Moby'])
# print(fish_inventory_cls.__iter__())
# for fish in fish_inventory_cls:
#     print(fish)

class CustomerCounter:
    def __init__(self, customerList):
        self.customers = customerList

    def __iter__(self):
        self.count = 0
        return self
    
    def __next__(self):
        if self.count > 99:
            raise StopIteration
        self.count += 1
        return self.count
        
# customer_cls = CustomerCounter(list(range(110)))

# for customer in customer_cls:
#     print(customer)
# fish_iter = iter(fish_inventory_cls)
# print(next(fish_iter))

from itertools import count, chain, combinations
# count(start,[step])
# for i in count(start=0, step=2):
#     print(i)
#     if i >= 20:
#         break

# chain(*iterables)
odd = [5, 7, 9]
even = {6, 8, 10}

# all_numbers = chain(odd, even) # iterator

# for number in all_numbers:
#     print(number)

# combinations(iterable, r)
even = [2, 4, 6]
even_combinations = list(combinations(even, 3))
# print(even_combinations)
# [(2, 4), (2, 6), (4, 6)]
collars = ['Red-s', 'Red-M', 'Blue-XS', 'Green-L', 'Green-XL', 'Yellow-M']
collar_combo_iterator = combinations(collars, 3)

# for collar in collar_combo_iterator:
#     print(collar)


# Generators
# print([i for i in range(100000)])

# generator expression
print((i for i in range(100000)))

def multiply(a, b):
    sum = 0
    return a * b

# print(multiply(2, 3))

def course_generator():
    yield 'Computer Science'
    yield 'Art' # 2
    yield 'Business' # 3

courses = course_generator()
# print(next(courses))
# print(next(courses))
# print(next(courses))
# for course in courses:
#     print(course)

# def fibbo(n):
#     if n == 1:
#         yield 0
#     if n == 2:
#         yield 1
#     return fibbo(n - 1) + fibbo(n - 2)

# fibbonacci = fibbo
# print(next(fibbonacci(3)))
# print(next(fibbonacci(4)))
# print(next(fibbonacci(5)))
# for fib in fibbonacci:
#     print(fib)

# def prize_generator():
#     student_info = {
#         'JJ': 355,
#         'BM': 45,
#         'TR': 18,
#         'KN': 25
#     }

#     for student in student_info:
#         name = student
#         id = student_info[name]
#         if id % 3 == 0 and id % 5 == 0:
#             yield student + ' gets prize C'
#         elif id % 3 == 0:
#             yield student + ' gets prize A'
#         elif id % 5 == 0:
#             yield student + ' gets prize B'

# prizes = prize_generator()
# for prize in prizes:
#     print(prize)


# def student_standing_generator():
#     student_standings = ['Freshman', 'Junior', 'Senior', 'Freshman']

#     for student in student_standings:
#         name = student
#         id = student_standings[]
#         if id == 500:
#             yield student[0]

# standings = student_standing_generator()
# for standing in standings:
#     print(standing)




def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print(next(fib))
print(next)

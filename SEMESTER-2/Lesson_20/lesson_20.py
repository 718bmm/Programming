# def mult(x, y, z):
#     print("args", x, y, z)
#     return x * y * z


numbers = [i for i in range(10)]
numbers_2 = [i for i in range(10, 15)]
numbers_3 = [i for i in range(20, 30)]
# print(list(map(mult, numbers, numbers_2, numbers_3)))


def find_even(x):
    return x % 2 == 0

# print(list(filter(lambda x: x % 2 == 0, numbers)))
# print(list(filter(find_even, numbers)))

names = ['retr', 'eer', 'w', 'ad']
def find_ss(names):
    if len(names) >= 3:
        return names
    
print(list(filter(lambda names: len(names) >= 3, names)))
print(list(filter(find_ss, names)))

# numbers = {i:str(i) for i in range(10)}
# numbers_2 = {i:str(i) for i in range(10, 15)}
# print(numbers)
# print("answer", list(zip(numbers.values(), numbers_2.values())))


# [2, [2 , 3, [[[[[[[[5]]]]]]]]]]
def fibbo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibbo(n - 1) + fibbo(n - 2)

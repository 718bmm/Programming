a = [2, [2 , 3, [[[[[[[[5]]]]]]]]]]

def rec(spicok, level=1):
    print(*spicok, 'level=', level)
    for i in spicok:
        if type(i) == list:
            rec(i, level + 1)

rec(a)

def filter_2(func, iterable):
    return [variable for variable in iterable if func(variable)]

names = ['retr', 'eer', 'w', 'ad']
def find_ss(names):
    if len(names) >= 3:
        return names
    
print(list(filter(lambda names: len(names) >= 3, names)))
print(list(filter(find_ss, names)))
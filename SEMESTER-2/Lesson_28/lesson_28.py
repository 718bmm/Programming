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
# print(re.search('specific',string))
# a = re.search('specific',string)
# print("group",a.group())
# print(a.span())
# print(a.start())
# print(a.end())

# a = pattern.search(string)
# print(a)
# b = pattern.findall(string)
# print(b)
# c = pattern.fullmatch(string)
# print(c)

pattern = re.compile(r"([a-zA-Z]).([p])") # a-zA-Z-любой-символ-должен заканчиватся буквой t

string = '123Look for pthe aspecific tword for if you can. :1'

# pattern = re.compile(r"([a-zA-Z]).([t])")

a = pattern.finditer(string)
print(next(a))
print(next(a))
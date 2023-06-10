import re


"""
e - matches "e" symbol (if used with g flag would match any number of e's in string).
    e+ - match "e" at least once, where + means match preceding character at least once or infinite.
    ea? - match "e" and "a", but a is optional.
    ea* - match "e" and "a", but a is optional and can be infinite.
    . - match anything except newline.
    \symbol - ignores regex symbols, making them match what they actually is. Example: \. - matches .
    \w - match any word character
    \s - match any space character
    \S - match anything which is not whitespace
    \W - match anything which is not character
    \w{4} - match exactly 4 matches of regex
    {4,5} - 4 or 5 matches. {4,} - 4 or more matches
    [fc]at - grouping. matches "f" or "c" and "at": fat or cat
    | - same as "or" logic operator in programming
    (t|e|r){2,3}\. - matches "t or e or r" with length 2 to 3 character ending with period.
    ^ - beginning of the string
    $ - end of the string
    \d - matches any digits
    \d{3}[ -]?\d{3}[ -]?\d{4}
    (\d{3})[ -]?(\d{3})[ -]?(\d{4}) - grouping
    (?<areacode>\d{3})[ -]?(\d{3})[ -]?(\d{4})
    ((\+1)[ -]?)?\(?(?<areacode>\d{3})\)?[ -]?(\d{3})[ -]?(\d{4})
"""

# titles = [
#     "Middle JavaScript Developer",
#     "Middle JavaScript Developer (AngularJS 9)",
#     "Middle JavaScript Developer (React)",
#     "Senior JavaScript Developer (Angular)",
#     "middle JavaScript angularjs "
# ]
# title = 'middle JavaScript React '

# js = {
#     'javascript': [
#         'javascript',
#         'angular',
#         'angularjs',
#         'react',
#         'node js',
#         'node.js',
#         'nodejs',
#     ],
# }
# mapper_string = "|".join([reg_ex for reg_ex in js['javascript']])
# result = re.finditer(mapper_string, title, re.IGNORECASE)
# print(next(result))
# print(next(result))


# regex = r'react|javascript|angular'

# test_str = r'middle javascript react'
# matches = list(re.findall(regex, test_str, re.MULTILINE))
# print(matches)
# for match in matches:
#     print('match, match.group()')

# print(len(matches))

# Password Checker
# pattern = r'(^[A-Z][a-z0-9$#@%]{6,}\d$)' # or type \d instead of [0-9]$
# password = 'Asomejokehere8'

# result = re.fullmatch(pattern, password)
# print(result)


# unittest
# pytest
# django


def plus(num):
    try:
        return int(num) + 5
    except ValueError as err:
        return err


num = 1
isinstance(num, int)
# raise ZeroDivisionError()
# assert condition, ""

if __name__ == '__main__':
    print(plus(5))
    print(plus('5'))
    print(plus('-1'))
    print(plus('a'))
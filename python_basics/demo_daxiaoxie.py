string = 'aBAFLADJKdfdZbg我们的你们的'
str_lowercase = string.lower()
# print(str_lowercase)
str_upper = string.upper()
# print(str_upper, type(str_upper))

import re
mystring = 'some string'
pattern = 'some'
# match = re.search(pattern, mystring, re.IGNORECASE)
# print(match)
# bool(match)

m = re.search('ZBg我', string, re.IGNORECASE)
print(m)
print(bool(m))

n = re.search('zBg', string, re.I)
print(n)
print(bool(n))

print(bool('Zbg' in string))




import re

pattern1 = '.'

str1 = 'a'
str2 = '_'
str3 = 'A'
str4 = '1'
str5 = '\n'

print(re.match(pattern1, str1) is not None)
print(re.match(pattern1, str2) is not None)
print(re.match(pattern1, str3) is not None)
print(re.match(pattern1, str4) is not None)
print(re.match(pattern1, str5) is not None)

print('*'*20)

pattern2 = '\d'

print(re.match(pattern2, str4) is not None)
print(re.match(pattern2, str1) is not None)
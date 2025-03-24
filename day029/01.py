import re

pattern1 = '\s'

str1 = ' '

print(re.match(pattern1, str1) is not None)

pattern2 = '1[3579]\d{9}'

str2 = '13999999999'

print(re.match(pattern2, str2))

pattern3 = '\w{8,20}'

str3 = 'aaaa1111'

print(re.match(pattern3, str3))

pattern4 = '[A-Z]\w*\d'

str4 = '111H7873dsdsd1'

print(re.search(pattern4, str4))
print(re.match(pattern4, str4))

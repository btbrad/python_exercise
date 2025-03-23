import re

if __name__ == '__main__':

    pattern1 = 'hello'

    str1 = 'Hello world'

    res1 = re.match(pattern1, str1, re.I)

    print(res1)
    if res1 is not None:
        print(res1.group())
        print(res1.span())
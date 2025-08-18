'''
设计一个生成验证码的函数。
'''

from random import choices
from string import ascii_letters, digits

ALL_CHARS = digits + ascii_letters

def generate_code(code_len = 4):
    return ''.join(choices(ALL_CHARS, k = code_len))

if __name__ == '__main__':
    for i in range(10): 
        print(generate_code(i))
'''
要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
'''
import re

username = input('请输入用户名：')
reg1 = '^[a-zA-Z0-9_]{6,20}$'

if re.match(reg1, username):
    print('用户名格式正确')
else:
    print('用户名格式错误')


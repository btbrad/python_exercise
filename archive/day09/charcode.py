'''
循环录入编码值打印文字，直到输入空字符串停止
'''

while True:
    code = input('请输入编码值：')
    if code != '':
        print(chr(int(code)))
    else:
        break

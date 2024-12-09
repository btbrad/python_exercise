'''
字符串： content = "我是京师监狱狱长金海。"
 打印第一个字符、打印最后一个字符、打印中间字符
 打印字前三个符、打印后三个字符
 命题：金海在字符串content中
 命题：京师监狱不在字符串content中
 通过切片打印“京师监狱狱长”
 通过切片打印“长狱狱监师京”
 通过切片打印“我师狱海”
 倒序打印字符
'''
content = '我是京师监狱狱长金海。'
print(f'打印第一个字符:{content[0]}')
print(f'打印最后一个字符:{content[-1]}')
print(f'打印中间字符:{content[len(content) // 2 - 1]}')
print(f'打印字前三个符：{content[0:3]}')
print(f'打印后三个字符: {content[-4:len(content):1]}')
bool1 = '金海' in content
print(f'金海在字符串content中:{bool1}')
bool2 = '京师监狱' not in content
print(f'京师监狱不在字符串content中:{bool2}')
print(f'{content[2:8]}')
print(f'{content[-4:1:-1]}')
print(f'{content[::3]}')
print(f'{content[::-1]}')
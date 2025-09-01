'''
用/（斜杠）分隔仅限位置参数与其它参数。/与参数之间用逗号分隔。/前是仅限位置参数。/前的参数不能用关键字传递。
'''

def test(a, /, b):
  print(a, b)

#test(a=1, b = 2)  # TypeError: test() got some positional-only arguments passed as keyword arguments: 'a'
test(1, b = 2)  # 1 2
test(1, 2)
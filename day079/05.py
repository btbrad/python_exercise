a = 5
b = 2

try:
  res = a / b
except ZeroDivisionError as e:
  print(f'除数为0异常: {e}')
except BaseException as e:
  print(f'未知异常: {e}')
else:
  print('没有异常')
finally:
  print('无论是否异常都会执行')      
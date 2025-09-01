'''
在函数内部修改全局变量，必须使用global
在嵌套函数中，如果需要修改外部函数的局部变量，可以使用nonlocal。
'''

a = 2

def fun():
  global a
  a = 5
  print(f'局部变量a:{a}')

fun()

print(f'全局变量a:{a}')

def outer():
  b = 2
  def inner():
    nonlocal b
    b = 5
    print(f'内部函数变量b: {b}')

  inner()
  print(f'外部函数变量b: {b}')  

outer()  
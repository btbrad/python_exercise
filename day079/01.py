'''
实参为不可变对象时，进行的是值传递。实参为可变对象时，进行的是引用传递。参数默认值为列表、字典或类实例等可变对象时，会导致错误的结果。
'''

def test(a, x=[]):
  x.append(a)
  return x

print(test(1))  
print(test(2))  
print(test(3))  
print(test(4))  

def test2(a, x=None):
    if x is None:
       x = []
    x.append(a)
    return x   

print(test2(1))  
print(test2(2))  
print(test2(3))  
print(test2(4)) 
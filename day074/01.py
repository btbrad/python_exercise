'''
猜数字
'''
from random import randint

target = randint(1, 100)
times = 0

while True:
  times += 1  
  guess = int(input("请重新输入1-100的整数："))
  if guess < target:
    print("猜小了")
  elif guess > target:
    print("猜大了")
  else:  
    print("猜对了")
    break

print(f'你猜了{times}次')

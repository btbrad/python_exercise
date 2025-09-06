import time

def count_down():
  print('倒计时10秒开始...')
  for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
  print('倒计时结束!')


if __name__ == '__main__':
  count_down()  

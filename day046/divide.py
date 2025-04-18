def play_divide():
  file_name = './day046/log.txt'

  print('输入两个整数，计算它们的商，输入q退出！')
  while True:
    num1 = input('请输入被除数：')
    if (num1 == 'q'):
      print('退出程序')
      break
    num2 = input('请输入除数：')
    if (num2 == 'q'):
      print('退出程序')
      break 
    try:
      result = int(num1) / int(num2)
      with open(file_name, 'a') as f:
        f.write(f'{num1} / {num2} = {int(num1) / int(num2)}\n')
    except ZeroDivisionError:
      print('0不能作为除数！')  
    else:
      print(f'商为{result}')

if __name__ == '__main__':
  play_divide()      
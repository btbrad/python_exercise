# 读取整个文件
with open('data.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# 逐行读取
with open('data.txt', 'r', encoding='utf-8') as f:
  for line in f:
      print(line.strip())# 去除换行符

# 列表读取
with open('data.txt', 'r', encoding='utf-8') as f:
  lines = f.readlines()
  for line in lines:
      print(line.strip())# 去除换行符      

# 写入文件 覆盖
with open('data.txt', 'w', encoding='utf-8') as f:
  f.write('hello world\n')      
  f.write('hello python\n')      

# 写入文件 追加
with open('data.txt', 'a', encoding='utf-8') as f:
  f.write('你好\n')      
  f.write('世界')    

# 写入文件 多行
lines = [f'第{n + 1}行文字\n' for n in range(5)]
with open('data.txt', 'w', encoding='utf-8') as f:
  f.writelines(lines)  

# 二进制模式 复制图片
imgData = ''
with open('test.jpg', 'rb') as f:
   imgData = f.read()

with open('test_copy.jpg', 'wb') as f:
   f.write(imgData)   

# 文件指针
with open('data.txt', 'r', encoding='utf-8') as f:
   print(f.tell())# 获取文件指针位置
   print(f.read(3))# 读取3个字符
   print(f.tell())# 获取文件指针位置
   f.seek(0)# 设置文件指针位置
   print(f.tell())# 获取文件指针位置
   print(f.read())# 读取剩余字符     
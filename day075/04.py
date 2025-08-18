'''
设计一个函数返回给定文件的后缀名
'''
def get_suffix(filename, ignore_dot=True):
  pos = filename.rfind('.')
  if pos <= 0:
    return ''
  return filename[pos + 1:] if ignore_dot else filename[pos:]

from os.path import splitext
def get_suffix2(filename, ignore_dot=True):
  return splitext(filename)[1] if not ignore_dot else splitext(filename)[1][1:]

if __name__ == '__main__':
  print(get_suffix('a.py'))
  print(get_suffix('a.py', False))
  print(get_suffix2('a.py'))
  print(get_suffix2('a.py', False))
import json

def load_user():
  file_name = './day046/user.txt'
  try:
    with open(file_name) as f:
      username = json.load(f)
  except FileNotFoundError:
    username = input('请输入用户名：')
    with open(file_name, 'w') as f:
      json.dump(username, f)
      print(f'记住你了！{ username }')
  else:
    print(f'欢迎回来！{ username }') 

if __name__ == '__main__':
  load_user()       
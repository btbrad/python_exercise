from Service import Service

if __name__ == '__main__':
  uname = input('请输入用户名:')
  password = input('请输入密码:')
  service = Service()
  if service.login(uname, password):
    print('登录成功')
  else:
    print('登录失败')  
from flask import Flask, session, request

app = Flask(__name__)

app.secret_key = 'secret'
@app.before_request
def before_request():
  url = request.path
  print(url)
  if url in ['/login/']:
    pass
  else:
    if session.get('isLogin'):
      pass
    else:
      return '请登录'

@app.route('/login/')
def login():
  session['isLogin'] = True
  return '登录成功！'

@app.route('/logout/')
def logout():
  session['isLogin'] = False
  return '退出登录！'

@app.route('/')
def index():
  return 'Hello Flask !'

if __name__ == '__main__':
  app.run(debug=True)
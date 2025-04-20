from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class PhoneConverter(BaseConverter):
    regex = '1[345789]\d{9}'

class InfoConverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')

app.url_map.converters['phone'] = PhoneConverter    
app.url_map.converters['info'] = InfoConverter    

@app.route('/')
def index():
    return 'Hello Flask !'

@app.route('/article/<int:id>')
def article(id):
    print(type(id))
    return f'文章{id}'

@app.route('/phone/<phone:params>')
def phone(params):
    print(type(params))
    return f'手机号{params}'

@app.route('/user/<info:params>')
def user_info(params):
    print(type(params))
    return f'用户信息{params}'

if __name__ == '__main__':
    app.run(port=9527, debug=True)
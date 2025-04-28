from flask import Flask
from flask_restful import Resource, Api, inputs, fields, marshal_with
from flask_restful.reqparse import RequestParser

app = Flask(__name__)

api = Api(app)

class LoginView(Resource):

    resource_fields = {
        'code': fields.Integer(default=1),
        'msg': fields.String,
        'data': fields.String(attribute='info')
    }

    @marshal_with(resource_fields)
    def get(self):
        return {'code': 1, 'msg': 'get login', 'info': '数据列表'}

    @marshal_with(resource_fields)
    def post(self):
        return {'msg': 'post login'}
    
api.add_resource(LoginView, '/login/')    

class RegisterView(Resource):
    def get(self):
        return {'msg': 'get register'}

    def post(self):
        parser = RequestParser()
        parser.add_argument('username', type=str, required=True, help='用户名不能为空！', trim=True)
        parser.add_argument('password', type=str, default='123456', trim=True)
        parser.add_argument('phone', type=inputs.regex('^1[3-9]\d{9}$'), required=True,  help='手机号码格式不正确！', trim=True)
        args = parser.parse_args()
        print(args)
        return {'msg': '注册成功'}
    
api.add_resource(RegisterView, '/register/')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, url_for
from flask.views import View

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask !'

def login():
    return 'Login'
app.add_url_rule('/login/', view_func=login, endpoint='login')

class ListView(View):
    def dispatch_request(self):
        return '这是一个列表视图'
    
app.add_url_rule('/list/', view_func=ListView.as_view('list'))    

with app.test_request_context():
    print(url_for('list'))

if __name__ == '__main__':
    app.run(debug=True)
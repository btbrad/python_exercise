from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'name': 'Flask',
        'age': 18,
        'gender': '男'
    }

    return render_template('index.html', info="Flask is working!", param=10.5, **context)

@app.route('/user/<int:id>')
def user(id):
    return f'用户{id}'

if __name__ == '__main__':
    app.run(debug=True)
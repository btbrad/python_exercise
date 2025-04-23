from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    username = 'ls'
    languages = ['python', 'java', 'c++']
    info={'name': 'bt', 'age': 18, 'sex': 'male'}
    return render_template('index.html', username=username, items=languages, info=info)

if __name__ == '__main__':
    app.run(debug=True)

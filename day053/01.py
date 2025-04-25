from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

from user import user_bp
app.register_blueprint(user_bp, url_prefix='/user/')

from login import login_bp
app.register_blueprint(login_bp, url_prefix="/login/")

if __name__ == '__main__':
    app.run(debug=True)

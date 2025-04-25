from user import user_bp
from flask import render_template

@user_bp.route('/')
def index():
    return render_template('index1.html')
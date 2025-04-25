from login import login_bp

@login_bp.route('/')
def login():
    return 'This is login page'
from blinker import Namespace
from flask import request, g

space = Namespace()
login_space = space.signal('login')

def login_signal(sender):
    ip = request.remote_addr
    info = f'{ip}: {g.name}'
    with open('login.log', 'a', encoding='utf-8') as f:
        f.write(info + '\n')

login_space.connect(login_signal)        
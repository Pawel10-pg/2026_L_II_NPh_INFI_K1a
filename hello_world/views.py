from hello_world import app
from flask import request

@app.route('/')
def index():
    name = request.args.get('name', 'Pawel')
    return '{"imie":"' + name + '", "msg":"Hello World!"}'

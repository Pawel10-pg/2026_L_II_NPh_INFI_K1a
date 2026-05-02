from flask import request, jsonify
from hello_world import app


@app.route('/')
def index():
    name = request.args.get('name', 'Pawel')
    return jsonify(imie=name, msg="Hello World!")

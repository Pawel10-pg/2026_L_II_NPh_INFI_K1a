from flask import request

def get_index():
    name = request.args.get('name')
    return f'{{ "imie":"{name}", "msg":"Hello World!" }}'

from flask import request


def get_index():
    name = request.args.get('name', 'Pawel')
    return '{"imie":"' + name + '", "msg":"Hello World!"}'

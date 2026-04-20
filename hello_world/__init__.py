# flake8: noqa
from flask import Flask

app = Flask(__name__)

import hello_world.views

# api/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    # config, routes, etc.
    return app

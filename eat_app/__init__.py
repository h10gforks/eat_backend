#coding:utf-8
import os
from flask import Flask


app = Flask(__name__)
    
from .api import api
app.register_blueprint(api, url_prefix="/api/v1.0")


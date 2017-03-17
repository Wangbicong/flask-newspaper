# -*- coding: utf-8 -*-
from newspaper import app


@app.route('/')
def index():
    return 'Hello World!'

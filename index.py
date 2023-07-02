#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")

def index():

    url = open('Google.html','r')

    return '''
        <font size="7" color="#000000"><u><b>This is Test</b></u></font>
        <h1>This is test</h1>

    '''


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
app = Flask(__name__, template_folder='template')


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(threaded=True,  debug=True, host='0.0.0.0')

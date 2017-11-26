#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
app = Flask(__name__, template_folder='template')


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/mvt", methods=['GET'])
def multivariate_test():
    return render_template('mvt.html')


@app.route("/redirect_test", methods=['GET'])
def redirect_test():
    return render_template('redirect_test.html')


@app.route("/redirect_test_new_page", methods=['GET'])
def redirect_test_new_page():
    return render_template('redirect_test_new_page.html')


if __name__ == "__main__":
    app.run(threaded=True,  debug=True, host='0.0.0.0')

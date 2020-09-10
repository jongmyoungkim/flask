from flask import Flask
from markupsafe import escape
from flask import render_template

from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return 'index - hello, world!'




@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


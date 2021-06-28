import datetime, math, decimal, pyrebase, urllib
import random
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session,g, abort
from NB import *

#Steps
# python -m venv venv
# .\venv\Scripts\Activate.ps1
# $env:FLASK_APP = "app.py"
# set FLASK_APP=app:myapp
# pip install flask pyrebase4 pandas nltk
# pip uninstall numpy
# pip install numpy ==1.19.3
# pip freeze > requirements.txt
# flask run

myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return render_template('index.html')


@myapp.route('/think', methods=['GET', 'POST'])
def exeThink():
    text = request.form['message']
    
    nn = NN()
    
    result = nn.think(text)
    return render_template('index.html', message=result)

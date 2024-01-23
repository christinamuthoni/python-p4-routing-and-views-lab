#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:hello>')
def print_string(hello):
    print (f"{hello}")

    return hello

@app.route('/count/<int:num>')
def count(num):
    numbers =  [i for i in range(num + 1)]
    return numbers
   
    
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)

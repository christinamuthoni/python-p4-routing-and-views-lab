#!/usr/bin/env python3

from flask import Flask, request

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
    numbers = list(range(num + 1))

    # Convert the list of numbers to a string with commas
    #numbers_str = ', '.join(map(str, numbers))
    #numbers_str = str(numbers).split('').join('')

    return numbers

@app.route('/math/<parameter>')
def math():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    operation = request.args.get('operation')

    if operation == '+':
        result = num1 + num2
        return str(result)
    else:
        return "Invalid operation"
    
    

if __name__ == '__main__':
    app.run(port=5553, debug=True)

#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join([str(i) for i in range(parameter)])
    return numbers + '\n', 200,{'Content-Type': 'text/plain'}

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero", 400
    elif operation == '%':
        if num2 !=0:
            result = num1 % num2
        else:
            return "Error: Division by zero", 400
    else:
        return "Error: Invalid operation", 400

    return str(result)    
    

from flask import Flask

from flask import request

 

app = Flask(__name__)

 

@app.route('/')

def hello():

    return '<h1>Hello, World, we are fine!</h1>'


@app.route('/sumar')
def sumar():
    param1 = int(request.args.get('param1', 0))
    param2 = int(request.args.get('param2', 0))
    result = param1 + param2
    return f'La suma es: {result}'

@app.route('/multiplicar')
def multiplicar():
    param1 = int(request.args.get('param1', 0))
    param2 = int(request.args.get('param2', 0))
    result = param1 * param2
    return f'El producto es: {result}'


if __name__ == 'main':
    app.run()
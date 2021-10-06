from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addNumbers():
  a =int(request.args.get("a"))
  b = int(request.args.get("b"))
  return str(add(a,b))

@app.route('/sub')
def subtractNumbers():
  a =int(request.args.get("a"))
  b = int(request.args.get("b"))
  return str(sub(a,b))

@app.route('/mult')
def multiplyNumbers():
  a =int(request.args.get("a"))
  b = int(request.args.get("b"))
  return str(mult(a,b))
  
@app.route('/div')
def divideNumbers():
  a =int(request.args.get("a"))
  b = int(request.args.get("b"))
  return str(div(a,b))
  



from flask import Flask, jsonify
from random import randint

from projects.calculator.calculator import Calculator

app = Flask(__name__)
my_calculator = Calculator()

@app.route('/')
def hello():
  num1 = randint(0, 100)
  num2 = randint(0, 100)
  result = my_calculator.add(num1, num2)
  response = {
    'num1': num1,
    'num2': num2,
    'result': result,
    'message': "Did you know {} + {} = {}?".format(num1, num2, result)
  }
  return jsonify(response)

if __name__ == '__main__':
  app.run(host='0.0.0.0')

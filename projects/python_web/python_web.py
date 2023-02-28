from flask import Flask, jsonify, render_template
from random import randint

from projects.calculator.calculator import Calculator

app = Flask(__name__)
my_calculator = Calculator()

def generate_random_calculation():
  num1 = randint(0, 100)
  num2 = randint(0, 100)
  result = my_calculator.add(num1, num2)
  return {
    'num1': num1,
    'num2': num2,
    'result': result,
    'message': "Did you know {} + {} = {}?".format(num1, num2, result)
  }

@app.route('/api/v1/')
def api_index():
  random_calculation = generate_random_calculation()
  return jsonify(random_calculation)

@app.route('/')
def web_index():
  random_calculation = generate_random_calculation()
  return render_template("index.html", **random_calculation)

if __name__ == '__main__':
  app.run(host='0.0.0.0')

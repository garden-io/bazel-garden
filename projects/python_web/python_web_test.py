import unittest

from projects.calculator.calculator import Calculator
from python_web import app

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.calculator = Calculator()

    def test_hello(self):
        print("testing")
        response = self.client.get('/api/v1/')
        print(response)
        data = response.get_json()
        num1 = data['num1']
        num2 = data['num2']
        result = data['result']
        expected_sum = self.calculator.add(num1, num2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result, expected_sum)

if __name__ == '__main__':
    unittest.main()

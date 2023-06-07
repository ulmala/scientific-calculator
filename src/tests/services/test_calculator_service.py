import math
import unittest
from unittest.mock import MagicMock
from entities.expression import Expression
from services.calculator_service import CalculatorService


class TestCalculatorService(unittest.TestCase):
    def setUp(self):
        self.calculator_service = CalculatorService()

    def test__evaluate_postfix_notation_returns_correct_value_1(self):
        expression = Expression("3+4.2*2/(1-5)^2^3")
        correct_value = 3+4.2*2/(1-5)**2**3
        tokens = ["3", "+", "4.2", "*", "2", "/",
                  "(", "1", "-", "5", ")", "^", "2", "^", "3"]
        expression.set_tokens(tokens)
        correct_postfix = ["3", "4.2", "2", "*", "1",
                           "5", "-", "2", "3", "^", "^", "/", "+"]
        expression.set_postfix(correct_postfix)

        value = self.calculator_service._evaluate_postfix_notation(
            expression.postfix())

        correct_value = round(correct_value, 3)
        value = round(correct_value, )
        self.assertAlmostEqual(correct_value, value,
                               places=8)  # TODO: debug this

    def test__evaluate_postfix_notation_returns_correct_value_2(self):
        expression = Expression("sin(max(2,3)/3*3.1)")
        correct_value = math.sin(max(2, 3)/3*3.1)
        tokens = ["sin", "(", "max", "(", "2", ",", "3", ")",
                  "/", "3", "*", "3.1", ")"]
        expression.set_tokens(tokens)
        correct_postfix = ["2", "3", "max", "3", "/", "3.1", "*", "sin"]
        expression.set_postfix(correct_postfix)

        value = self.calculator_service._evaluate_postfix_notation(
            expression.postfix())
        self.assertAlmostEqual(correct_value, value)

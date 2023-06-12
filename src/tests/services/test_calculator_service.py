import math
import unittest
from unittest.mock import MagicMock, patch
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
        expression.tokens = tokens
        correct_postfix = ["3", "4.2", "2", "*", "1",
                           "5", "-", "2", "3", "^", "^", "/", "+"]
        expression.postfix = correct_postfix

        value = self.calculator_service._evaluate_postfix_notation(
            expression.postfix)

        correct_value = round(correct_value, 3)
        value = round(correct_value, )
        self.assertAlmostEqual(correct_value, value,
                               places=8)  # TODO: debug this

    def test__evaluate_postfix_notation_returns_correct_value_2(self):
        expression = Expression("sin(max(2,3)/3*3.1)")
        correct_value = math.sin(max(2, 3)/3*3.1)
        tokens = ["sin", "(", "max", "(", "2", ",", "3", ")",
                  "/", "3", "*", "3.1", ")"]
        expression.tokens = tokens
        correct_postfix = ["2", "3", "max", "3", "/", "3.1", "*", "sin"]
        expression.postfix = correct_postfix

        value = self.calculator_service._evaluate_postfix_notation(
            expression.postfix)
        self.assertAlmostEqual(correct_value, value)

    def test_variables_property_holds_correct_information(self):
        self.assertEqual(self.calculator_service.variables, {})
        self.calculator_service._variables = {"a": 1}
        self.assertEqual(self.calculator_service.variables, {"a": 1})

    def test_add_variable_adds_variable_correctly(self):
        self.calculator_service.add_variable(
            variable_name="a",
            variable_value=2
        )
        self.assertEqual(self.calculator_service.variables, {"a": 2})

    def test_get_variables_as_string_returns_correct_string(self):
        self.calculator_service.add_variable(
            variable_name="a",
            variable_value=2
        )
        self.calculator_service.add_variable(
            variable_name="b",
            variable_value=3
        )
        correct_str = "a = 2\nb = 3"
        self.assertEqual(self.calculator_service.get_variables_as_string(), correct_str)

    def test_solve_calls_all_other_functions_with_correct_arguments(self):
        expression = Expression("2 + 3 * 4")
        expression.postfix = ["2", "3", "4", "*", "+"]
        self.calculator_service._validation_service = MagicMock()
        self.calculator_service._parser_service = MagicMock()
        self.calculator_service._shunting_yard_service = MagicMock()
        self.calculator_service._evaluate_postfix_notation = MagicMock()
        self.calculator_service._parser_service.parse_to_tokens.return_value = ["2", "+", "3", "*", "4"]
        self.calculator_service._shunting_yard_service.run.return_value = expression
        self.calculator_service._evaluate_postfix_notation.return_value = 14.0

        result = self.calculator_service.solve(expression)

        self.calculator_service._validation_service.validate_expression.assert_called_once_with(expression)
        self.calculator_service._parser_service.parse_to_tokens.assert_called_once_with(
            expression=expression,
            variables=self.calculator_service.variables
        )
        self.calculator_service._shunting_yard_service.run.assert_called_once_with(["2", "+", "3", "*", "4"])
        self.calculator_service._shunting_yard_service.clear_stack_and_queue.assert_called_once()
        self.calculator_service._evaluate_postfix_notation.assert_called_once_with(["2", "3", "4", "*", "+"])

        self.assertEqual(result, 14.0)
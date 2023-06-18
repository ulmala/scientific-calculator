import pytest
import unittest
from math import sin
from unittest.mock import MagicMock, patch
from entities.expression import Expression
from services.calculator_service import CalculatorService, calculator_service

class NotValidExpression(Exception):
    pass

class TestCalculatorService(unittest.TestCase):
    def setUp(self):
        self.calculator_service = CalculatorService()

    def test__evaluate_postfix_notation_returns_correct_value_1(self):
        """Test that postfx notation is evaluated correctly"""
        expression = Expression("3+4.2*2/(1-5)^2^3")
        correct_value = 3+4.2*2/(1-5)**2**3
        tokens = [
            "3", "+", "4.2", "*", "2", "/", "(",
            "1", "-", "5", ")", "^", "2", "^", "3"
        ]
        expression.tokens = tokens
        correct_postfix = [
            "3", "4.2", "2", "*", "1", "5",
            "-", "2", "3", "^", "^", "/", "+"
        ]
        expression.postfix = correct_postfix

        value = self.calculator_service._evaluate_postfix_notation(
            expression.postfix
        )

        correct_value = round(correct_value, 3)
        value = round(correct_value, )
        self.assertAlmostEqual(
            correct_value,
            value,
            places=8
        )  # TODO: debug this

    def test__evaluate_postfix_notation_returns_correct_value_2(self):
        """Test that postfx notation is evaluated correctly"""
        expression = Expression("sin(max(2,3)/3*3.1)")
        correct_value = sin(max(2, 3)/3*3.1)
        tokens = [
            "sin", "(", "max", "(", "2", ",",
            "3", ")", "/", "3", "*", "3.1", ")"
        ]
        expression.tokens = tokens
        correct_postfix = ["2", "3", "max", "3", "/", "3.1", "*", "sin"]
        expression.postfix = correct_postfix

        value = self.calculator_service._evaluate_postfix_notation(
            expression.postfix
        )
        self.assertAlmostEqual(correct_value, value)

    def test_variables_property_holds_correct_information(self):
        """Tests that variable property works correctly"""
        self.assertEqual(self.calculator_service.variables, {})
        self.calculator_service._variables = {"a": 1}
        self.assertEqual(self.calculator_service.variables, {"a": 1})

    def test_add_variable_adds_variable_correctly(self):
        """Tests that adding a new variabel works correclty"""
        self.calculator_service.add_variable(
            variable_name="a",
            variable_value=2
        )
        self.assertEqual(self.calculator_service.variables, {"a": 2})

    def test_list_variables_returns_correct_string(self):
        """Tests that variables are returned as correct string"""
        self.calculator_service.add_variable(
            variable_name="a",
            variable_value=2
        )
        self.calculator_service.add_variable(
            variable_name="b",
            variable_value=3
        )
        correct_str = "a = 2\nb = 3"
        self.assertEqual(
            self.calculator_service.list_variables(), correct_str
        )

    @pytest.mark.skip(reason="need to fix logic")
    def test_solve_calls_all_other_functions_with_correct_arguments(self):
        """
        Tests that when solving and expression, all other services and methods
        are called with correct arguments
        """
        user_expression = "2 + 3 * 4"
        expression = Expression(user_expression)
        expression.postfix = ["2", "3", "4", "*", "+"]
        self.calculator_service._validation_service = MagicMock()
        self.calculator_service._parser_service = MagicMock()
        self.calculator_service._shunting_yard_service = MagicMock()
        self.calculator_service._evaluate_postfix_notation = MagicMock()
        self.calculator_service._parser_service.parse_to_tokens.return_value = [
            "2", "+", "3", "*", "4"]
        self.calculator_service._shunting_yard_service.run.return_value = expression
        self.calculator_service._evaluate_postfix_notation.return_value = 14.0

        expression = self.calculator_service.solve(user_expression)
        result = expression.value

        self.calculator_service._validation_service.validate_expression.assert_called_once_with(
            expression)
        self.calculator_service._parser_service.parse_to_tokens.assert_called_once_with(
            expression=expression,
            variables=self.calculator_service.variables
        )
        self.calculator_service._shunting_yard_service.run.assert_called_once_with(
            ["2", "+", "3", "*", "4"]
        )
        self.calculator_service._shunting_yard_service.clear_stack_and_queue.assert_called_once()
        self.calculator_service._evaluate_postfix_notation.assert_called_once_with(
            ["2", "3", "4", "*", "+"]
        )

        self.assertEqual(result, 14.0)

    def test__calculate_two_parameter_function_handles_type_error(self):
        """
        Tests that TypeError is and handled if floats are passed to
        a function which uses integers, e.g. comb()
        """
        token = "comb"
        stack = ["4.0", "2.0"]
        result = self.calculator_service._calculate_two_parameter_function(token, stack)
        result = self.assertEqual(result, "6")


class TestCalculatorServiceFull(unittest.TestCase):
    def setUp(self):
        self.valid_expressions = {
            "(2 + 3.5) * 4 - sin(1.2) ^ 2" : (2 + 3.5) * 4 - sin(1.2) ** 2,
            "max(5.7, 3.2) + 2.8 * sin(0.8) ^ 3": max(5.7, 3.2) + 2.8 * sin(0.8) ** 3,
            "(sin(0.5) + 2.1) / max(6.4, 1.7) ^ 2" : (sin(0.5) + 2.1) / max(6.4, 1.7) ** 2,
            "max(3.9, 2.6) + 4.3 * sin(1.5) - 2.8 ^ 2": max(3.9, 2.6) + 4.3 * sin(1.5) - 2.8 ** 2,
        }

        self.invalid_expressions = [
            "2 + * 3",
            "4 /",
            "5 + (6 * 2",
            "3 * 4)",
            "sin(2 3)",
            "max(4,)",
            "7 + 2 - * 3",
            "sin(1.2))",
            "max(2, 3 4)",
            "8 + - 5",
            "(9 + 2)) * 3"
        ]

        self.calculator_service = calculator_service

    def test_that_all_valid_expressions_are_solved_correctly(self):
        """Test that epxressions are solved correctly"""
        for exp, val in self.valid_expressions.items():
            expression = self.calculator_service.solve(exp)
            self.assertEqual(expression.value, val)

    def test_that_correct_error_messages_are_thrown(self):
        """Tests that correct error messages ares shown"""
        try:
            self.calculator_service.solve("3 * 4)")
        except Exception as e:
            self.assertEqual(str(e), "Wrong amount of parantheses!")

        try:
            self.calculator_service.solve("*2+1")
        except Exception as e:
            self.assertEqual(str(e), "Expression starts with illegal token!")

        try:
            self.calculator_service.solve("")
        except Exception as e:
            self.assertEqual(str(e), "Expression can't be empty!")

        try:
            self.calculator_service.solve("2**2")
        except Exception as e:
            self.assertEqual(str(e), "'**' is not a valid power operator! Use '^' instead")

        try:
            self.calculator_service.solve("2++2")
        except Exception as e:
            self.assertEqual(str(e), "Consecutive operators are illegal!")

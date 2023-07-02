import unittest
from unittest.mock import MagicMock
from entities.expression import Expression
from services.parser_service import ParserService


class TestParserService(unittest.TestCase):
    def setUp(self):
        self.parser_service = ParserService()

    def test_parse_to_tokens_parses_expressions_correctly(self):
        """Tests that raw expression is correctly parsed into tokens"""
        expressions = [
            (Expression("2+(10-1)"), ["2", "+", "(", "10", "-", "1", ")"]),
            (Expression("sin(2/3*4)+max(1.1,2)"),
             ["sin", "(", "2", "/", "3", "*", "4", ")", "+", "max", "(", "1.1", ",", "2", ")"]),
            (Expression("3/4*2+1-2^4"),
             ["3", "/", "4", "*", "2", "+", "1", "-", "2", "^", "4"])
        ]
        variables = {}
        for entry in expressions:
            expression = self.parser_service.parse_to_tokens(
                entry[0], variables)
            tokens = expression.tokens
            self.assertEqual(entry[1], tokens)

    def test__convert_variables_to_values_returns_same_tokens_if_no_variables_defined(self):
        """Tests that if no variables are defined, same tokens are returned"""
        tokens = ["1", "+", "1"]
        variables = {}
        self.assertEqual(
            self.parser_service._convert_variables_to_values(
                tokens, variables
            ),
            tokens
        )

    def test__convert_variables_to_values_converts_variables_to_values_if_variables_defined(self):
        """Tests that user defined variables are convert into their values correctyl"""
        tokens = ["a", "+", "1"]
        variables = {"a": "2"}
        self.assertEqual(
            self.parser_service._convert_variables_to_values(
                tokens, variables),
            ["2", "+", "1"]
        )

    def test__add_leading_zero_if_starting_with_minus(self):
        expression = Expression("-1+1")
        expression = self.parser_service._add_leading_zero_if_starting_with_minus(
            expression)
        self.assertEqual(expression.raw_expression[0], "0")

    def test__replace_negative_exponent_by_alternative_form(self):
        expression = Expression("2^(-3)+1*2^3")
        expression = self.parser_service._replace_negative_exponent_by_alternative_form(
            expression)
        self.assertEqual(expression.raw_expression, "1/(2^3.0)+1*2^3")

    def test_parse_to_tokens_calls_all_submethods_with_correct_arguments(self):
        expression = Expression("-1 + 2^(-3)")
        variables = {}
        self.parser_service._remove_whitespaces = MagicMock(
            return_value=expression)
        self.parser_service._add_leading_zero_if_starting_with_minus = MagicMock(
            return_value=expression)
        self.parser_service._replace_negative_exponent_by_alternative_form = MagicMock(
            return_value=expression)
        self.parser_service._get_tokens = MagicMock(
            return_value=["0", "-", "1", "+", "1", "/", "(", "2", "^", "3", ")"])
        self.parser_service._validation_service.check_if_tokens_are_not_dropped = MagicMock()
        self.parser_service._convert_variables_to_values = MagicMock(
            return_value=["0", "-", "1", "+", "1", "/", "(", "2", "^", "3", ")"])

        result = self.parser_service.parse_to_tokens(expression, variables)

        self.parser_service._remove_whitespaces.assert_called_once_with(
            expression)
        self.parser_service._add_leading_zero_if_starting_with_minus.assert_called_once_with(
            expression)
        self.parser_service._replace_negative_exponent_by_alternative_form.assert_called_once_with(
            expression)
        self.parser_service._get_tokens.assert_called_once_with(
            expression, variables)
        self.parser_service._validation_service.check_if_tokens_are_not_dropped.assert_called_once_with(
            self.parser_service._get_tokens.return_value, expression
        )
        self.parser_service._convert_variables_to_values.assert_called_once_with(
            self.parser_service._get_tokens.return_value, variables
        )

        self.assertEqual(result, expression)

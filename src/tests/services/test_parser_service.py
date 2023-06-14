import unittest
from unittest.mock import MagicMock
from entities.expression import Expression
from services.parser_service import ParserService


class TestParserService(unittest.TestCase):
    def setUp(self):
        self.parser_service = ParserService()

    def test_parse_to_tokens_parses_expressions_correctly(self):
        expressions = [
            (Expression("2+(10-1)"), ["2", "+", "(", "10", "-", "1", ")"]),
            (Expression("sin(2/3*4)+max(1.1,2)"),
             ["sin", "(", "2", "/", "3", "*", "4", ")", "+", "max", "(", "1.1", ",", "2", ")"]),
             (Expression("3/4*2+1-2**4"), ["3", "/", "4", "*", "2", "+", "1", "-", "2", "^", "4"])
        ]
        variables = {}
        for entry in expressions:
            expression = self.parser_service.parse_to_tokens(
                entry[0], variables)
            tokens = expression.tokens
            self.assertEqual(entry[1], tokens)

    def test__convert_variables_to_values_returns_same_tokens_if_no_variables_defined(self):
        tokens = ["1", "+", "1"]
        variables = {}
        self.assertEqual(
            self.parser_service._convert_variables_to_values(
                tokens, variables),
            tokens
        )

    def test__convert_variables_to_values_converts_variables_to_values_if_variables_defined(self):
        tokens = ["a", "+", "1"]
        variables = {"a": "2"}
        self.assertEqual(
            self.parser_service._convert_variables_to_values(
                tokens, variables),
            ["2", "+", "1"]
        )

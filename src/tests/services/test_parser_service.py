import unittest
from unittest.mock import MagicMock
from entities.expression import Expression
from services.parser_service import ParserService


class TestParserService(unittest.TestCase):
    def setUp(self):
        self.parser_service = ParserService()

    def test__expression_starts_with_digit(self):
        valid_expression = Expression("2+1")
        invalid_expression = Expression("+1")
        self.assertTrue(self.parser_service._expression_starts_with_digit(valid_expression))
        self.assertFalse(self.parser_service._expression_starts_with_digit(invalid_expression))

    def test__expression_starts_with_left_paranthesis(self):
        valid_expression = Expression("(1+1)")
        invalid_expression = Expression("1+1")
        self.assertTrue(self.parser_service._expression_starts_with_left_paranthesis(valid_expression))
        self.assertFalse(self.parser_service._expression_starts_with_left_paranthesis(invalid_expression))

    def test__expression_starts_with_valid_token(self):
        valid_expressions = [
            Expression("1+1"),
            Expression("(1+1)")
        ]
        invalid_expression = Expression("+3-1")
        for valid_expression in valid_expressions:
            self.assertTrue(self.parser_service._expression_starts_with_valid_token(valid_expression))
        self.assertFalse(self.parser_service._expression_starts_with_valid_token(invalid_expression))
        
    def test_validate_expression_returns_true_if_all_validations_passed(self):
        expression = Expression("(1+1)")
        self.assertTrue(self.parser_service.validate_expression(expression))


    def test_validate_expression_returns_false_if_any_validation_fails(self):
        expression = Expression("+3-1")
        self.assertFalse(self.parser_service.validate_expression(expression))

    def test_parse_to_tokens_parsers_expression_correctly(self):
        expression = Expression("2+(10-1)")
        correct_tokens = ["2", "+", "(", "10", "-", "1", ")"]
        expression = self.parser_service.parse_to_tokens(expression)
        tokens = expression.tokens()
        self.assertEqual(correct_tokens, tokens)

    def test_parse_to_tokens_calls_set_tokens_with_correct_args(self):
        expression = Expression("1+1")
        expression.set_tokens = MagicMock()
        self.parser_service.parse_to_tokens(expression)
        expression.set_tokens.assert_called_once_with(["1", "+", "1"])
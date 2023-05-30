import unittest
from unittest.mock import MagicMock
from entities.equation import Equation
from services.parser_service import ParserService


class TestParserService(unittest.TestCase):
    def setUp(self):
        self.parser_service = ParserService()

    def test__equation_starts_with_digit(self):
        valid_equation = Equation("2+1")
        invalid_equation = Equation("+1")
        self.assertTrue(self.parser_service._equation_starts_with_digit(valid_equation))
        self.assertFalse(self.parser_service._equation_starts_with_digit(invalid_equation))

    def test__equation_starts_with_left_paranthesis(self):
        valid_equation = Equation("(1+1)")
        invalid_equation = Equation("1+1")
        self.assertTrue(self.parser_service._equation_starts_with_left_paranthesis(valid_equation))
        self.assertFalse(self.parser_service._equation_starts_with_left_paranthesis(invalid_equation))

    def test__equation_starts_with_valid_token(self):
        valid_equations = [
            Equation("1+1"),
            Equation("(1+1)")
        ]
        invalid_equation = Equation("+3-1")
        for valid_equation in valid_equations:
            self.assertTrue(self.parser_service._equation_starts_with_valid_token(valid_equation))
        self.assertFalse(self.parser_service._equation_starts_with_valid_token(invalid_equation))
        
    def test_validate_equation_returns_true_if_all_validations_passed(self):
        equation = Equation("(1+1)")
        self.assertTrue(self.parser_service.validate_equation(equation))


    def test_validate_equation_returns_false_if_any_validation_fails(self):
        equation = Equation("+3-1")
        self.assertFalse(self.parser_service.validate_equation(equation))

    def test_parse_to_tokens_parsers_equation_correctly(self):
        equation = Equation("2+(10-1)")
        correct_tokens = ["2", "+", "(", "10", "-", "1", ")"]
        equation = self.parser_service.parse_to_tokens(equation)
        tokens = equation.tokens()
        self.assertEqual(correct_tokens, tokens)

    def test_parse_to_tokens_calls_set_tokens_with_correct_args(self):
        equation = Equation("1+1")
        equation.set_tokens = MagicMock()
        self.parser_service.parse_to_tokens(equation)
        equation.set_tokens.assert_called_once_with(["1", "+", "1"])
import unittest
from unittest.mock import MagicMock
from entities.expression import Expression
from services.validation_service import ValidationService


class TestValidationService(unittest.TestCase):
    def setUp(self):
        self.validation_service = ValidationService()

    def test_expression_starts_with_digit(self):
        valid_expression = Expression("2+1")
        invalid_expression = Expression("+1")
        self.assertTrue(
            self.validation_service.expression_starts_with_digit(valid_expression))
        self.assertFalse(
            self.validation_service.expression_starts_with_digit(invalid_expression))
        
    def test_expression_starts_with_left_paranthesis(self):
        valid_expression = Expression("(1+1)")
        invalid_expression = Expression("1+1")
        self.assertTrue(
            self.validation_service.expression_starts_with_left_paranthesis(valid_expression))
        self.assertFalse(self.validation_service.expression_starts_with_left_paranthesis(
            invalid_expression))
        
    @unittest.skip(reason="not implemented")
    def test__expression_starts_with_valid_token(self):
        valid_expressions = [
            Expression("1+1"),
            Expression("(1+1)")
        ]
        invalid_expression = Expression("+3-1")
        for valid_expression in valid_expressions:
            self.assertTrue(
                self.validation_service._expression_starts_with_valid_token(valid_expression))
        self.assertFalse(
            self.validation_service._expression_starts_with_valid_token(invalid_expression))
        
    def test_validate_expression_returns_true_if_all_validations_passed(self):
        expression = Expression("(1+1)")
        self.assertTrue(self.validation_service.validate_expression(expression))

    @unittest.skip(reason="not implemented")
    def test_validate_expression_returns_false_if_any_validation_fails(self):
        expression = Expression("+3-1")
        self.assertFalse(self.validation_service.validate_expression(expression))

    def test__is_operator_returns_true_if_operator(self):
        self.assertTrue(self.validation_service.is_operator("-"))
        self.assertTrue(self.validation_service.is_operator("+"))
        self.assertTrue(self.validation_service.is_operator("/"))
        self.assertTrue(self.validation_service.is_operator("*"))

    def test__is_operator_returns_false_if_not_operator(self):
        self.assertFalse(self.validation_service.is_operator("2"))
        self.assertFalse(self.validation_service.is_operator("200"))

    def test__is_left_associative_returns_true_if_operator_left_associative(self):
        self.assertTrue(self.validation_service.is_left_associative("-"))
        self.assertTrue(self.validation_service.is_left_associative("+"))
        self.assertTrue(self.validation_service.is_left_associative("/"))
        self.assertTrue(self.validation_service.is_left_associative("*"))

    def test__is_left_associative_returns_false_if_operator_not_left_associative(self):
        self.assertFalse(self.validation_service.is_left_associative("^"))
import unittest
from unittest.mock import MagicMock
from entities.expression import Expression
from services.validation_service import ValidationService
from services.validation_service import NotValidExpression


class TestValidationService(unittest.TestCase):
    def setUp(self):
        self.validation_service = ValidationService()

    def test_expression_starts_with_number(self):
        valid_expression = Expression("2+1")
        invalid_expression = Expression("+1")
        self.assertTrue(
            self.validation_service._expression_starts_with_number(valid_expression))
        self.assertFalse(
            self.validation_service._expression_starts_with_number(invalid_expression))

    def test_expression_starts_with_left_paranthesis(self):
        valid_expression = Expression("(1+1)")
        invalid_expression = Expression("1+1")
        self.assertTrue(
            self.validation_service._expression_starts_with_left_paranthesis(valid_expression))
        self.assertFalse(self.validation_service._expression_starts_with_left_paranthesis(
            invalid_expression))

    def test_validate_expression_does_not_raise_error_if_one_of_the_validations_is_passed(self):
        expressions = [
            Expression("(1+1)"),
            Expression("1+1"),
            Expression("sin(90)"),
            Expression("+1+1"),
            Expression("-1+1"),
        ]
        for expression in expressions:
            self.assertIsNone(
                self.validation_service.validate_expression(expression))

    def test_validate_expression_raises_error_if_all_validations_fail(self):
        expressions = [
            Expression("?1+1"),
            Expression(")1+1")
        ]
        for expression in expressions:
            with self.assertRaises(NotValidExpression):
                self.validation_service.validate_expression(expression)

    def test_is_operator_returns_true_if_operator(self):
        self.assertTrue(self.validation_service.is_operator("-"))
        self.assertTrue(self.validation_service.is_operator("+"))
        self.assertTrue(self.validation_service.is_operator("/"))
        self.assertTrue(self.validation_service.is_operator("*"))

    def test_is_operator_returns_false_if_not_operator(self):
        self.assertFalse(self.validation_service.is_operator("2"))
        self.assertFalse(self.validation_service.is_operator("200"))

    def test_is_left_associative_returns_true_if_operator_left_associative(self):
        self.assertTrue(self.validation_service.is_left_associative("-"))
        self.assertTrue(self.validation_service.is_left_associative("+"))
        self.assertTrue(self.validation_service.is_left_associative("/"))
        self.assertTrue(self.validation_service.is_left_associative("*"))

    def test_is_left_associative_returns_false_if_operator_not_left_associative(self):
        self.assertFalse(self.validation_service.is_left_associative("^"))

    def test__matching_parantheses_does_not_raise_error_if_matching_parantheses(self):
        expression = Expression("((1+2)*3)")
        self.assertIsNone(
            self.validation_service._matching_parantheses(expression))
        expression = Expression("(1+1)")
        self.assertIsNone(
            self.validation_service._matching_parantheses(expression))

    def test__matching_parantheses_raises_error_if_mismatching_parantheses(self):
        expression = Expression("((1+1)")
        with self.assertRaises(NotValidExpression):
            self.validation_service._matching_parantheses(expression)
        expression = Expression("1+1)")
        with self.assertRaises(NotValidExpression):
            self.validation_service._matching_parantheses(expression)

    def test_is_valid_variable_name_return_false_if_not_valid_variable_name(self):
        self.assertFalse(self.validation_service.is_valid_variable_name("?"))
        self.assertFalse(self.validation_service.is_valid_variable_name("a2"))
        self.assertFalse(self.validation_service.is_valid_variable_name("2"))
        self.assertFalse(self.validation_service.is_valid_variable_name("2a"))
        self.assertFalse(self.validation_service.is_valid_variable_name("sin"))

    def test_is_valid_variable_name_returns_true_if_valid_variable_name(self):
        self.assertTrue(self.validation_service.is_valid_variable_name("a"))
        self.assertTrue(self.validation_service.is_valid_variable_name("b"))
        self.assertTrue(self.validation_service.is_valid_variable_name("ab"))

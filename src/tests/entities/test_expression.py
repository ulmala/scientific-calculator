import unittest
from entities.expression import Expression


class TestExpression(unittest.TestCase):
    def setUp(self):
        self.expression = Expression("1+1")

    def test_constructor_sets_raw_expression_correctly(self):
        self.assertEqual(self.expression._raw_expression, "1+1")

    def test_raw_expression_returns_correct_value(self):
        self.assertEqual(self.expression.raw_expression, "1+1")

    def test_expression_has_empty_tokens_list_when_initiated(self):
        expression = Expression("1+1")
        self.assertEqual(expression.tokens, [])

    def test_set_tokens_sets_correct_values(self):
        tokens = ["1", "+", "1"]
        self.expression.tokens = tokens
        self.assertEqual(tokens, self.expression.tokens)

    def test_postfix_returns_correct_value(self):
        self.expression.postfix = ["+34"]
        self.assertEqual(["+34"], self.expression.postfix)

    def test_set_postfix_sets_value_to_class_variable(self):
        self.assertEqual(self.expression._postfix_notation, None)
        self.expression.postfix = ["+34"]
        self.assertEqual(self.expression._postfix_notation, ["+34"])

    def test_set_value_sets_value_to_class_varibale(self):
        self.assertEqual(self.expression._value, None)
        self.expression.value = 2
        self.assertEqual(2, self.expression._value)

    def test_str_representation(self):
        self.expression._tokens = ["1", "+", "1"]
        self.expression._postfix_notation = ["+", "1", "1"]
        correct_str = f"raw expression: 1+1\ntokens: ['1', '+', '1']\npostfix notation: ['+', '1', '1']"
        self.assertEqual(correct_str, str(self.expression))

    def test_raw_expression_setter_sets_value_to_correct_variable(self):
        self.expression.raw_expression = "2+2"
        self.assertEqual("2+2", self.expression.raw_expression)

    def test_property_value_returns_correct_value(self):
        self.expression.value = 0.0
        self.assertEqual(0.0, self.expression.value)

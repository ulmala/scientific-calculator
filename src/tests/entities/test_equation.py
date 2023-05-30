import unittest
from entities.expression import Expression


class TestExpression(unittest.TestCase):
    def setUp(self):
        self.expression = Expression("1+1")

    def test_constructor_sets_raw_expression_correctly(self):
        self.assertEqual(self.expression._raw_expression, "1+1")

    def test_raw_expression_returns_correct_value(self):
        self.assertEqual(self.expression.raw_expression(), "1+1")

    def test_expression_has_empty_tokens_list_when_initiated(self):
        expression = Expression("1+1")
        self.assertEqual(expression.tokens(), [])

    def test_set_tokens_sets_correct_values(self):
        tokens = ["1", "+", "1"]
        self.expression.set_tokens(tokens)
        self.assertEqual(tokens, self.expression.tokens())
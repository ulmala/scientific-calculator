import unittest
from entities.equation import Equation


class TestEquation(unittest.TestCase):
    def setUp(self):
        self.equation = Equation("1+1")

    def test_constructor_sets_raw_equation_correctly(self):
        self.assertEqual(self.equation._raw_equation, "1+1")

    def test_raw_equation_returns_correct_value(self):
        self.assertEqual(self.equation.raw_equation(), "1+1")

    def test_equation_has_empty_tokens_list_when_initiated(self):
        equation = Equation("1+1")
        self.assertEqual(equation.tokens(), [])

    def test_set_tokens_sets_correct_values(self):
        tokens = ["1", "+", "1"]
        self.equation.set_tokens(tokens)
        self.assertEqual(tokens, self.equation.tokens())
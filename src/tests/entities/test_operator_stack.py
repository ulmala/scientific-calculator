import unittest
from entities.operator_stack import OperatorStack


class TestOperatorStack(unittest.TestCase):
    def setUp(self):
        self.operator_stack = OperatorStack()

    def test_operator_stack_is_empty_after_init(self):
        self.assertEqual([], self.operator_stack._stack)

    def test_is_empty_returns_true_when_stack_is_empty_otherwise_false(self):
        self.assertTrue(self.operator_stack.is_empty())
        self.operator_stack._stack = ["+"]
        self.assertFalse(self.operator_stack.is_empty())

    def test_top_operator_returns_correct_value(self):
        self.operator_stack._stack = ["+", "-"]
        self.assertEqual("-", self.operator_stack.top_operator())

    def test_push(self):
        self.operator_stack.push("+")
        self.operator_stack.push("-")
        self.operator_stack.push("*")
        self.assertEqual(["+", "-", "*"], self.operator_stack._stack)

    def test_pop_pops_correct_value(self):
        self.operator_stack.push("+")
        popped_value = self.operator_stack.pop()
        self.assertEqual("+", popped_value)

    def test_pop_returns_none_if_stack_is_empty(self):
        popped_value = self.operator_stack.pop()
        self.assertEqual(None, popped_value)

    def test_top_operator_precedence_returns_correct_value(self):
        self.operator_stack.push("+")
        top_operator_precedence = self.operator_stack.top_operator_precedence()
        self.assertEqual(1, top_operator_precedence)

    def test_str_repr_returns_stack_as_string(self):
        self.operator_stack.push("+")
        self.operator_stack.push("-")
        self.assertEqual("['+', '-']", str(self.operator_stack))
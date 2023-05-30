import unittest
from unittest.mock import MagicMock
from entities.expression import Expression
from services.shunting_yard_service import ShuntingYardService


class TestShuntingYardService(unittest.TestCase):
    def setUp(self):
        self.shunting_yard_service = ShuntingYardService()

    def test__operator_precedence_returns_correct_value(self):
        self.assertEqual(
            1,
            self.shunting_yard_service._operator_precedence("-")
        )
        self.assertEqual(
            1,
            self.shunting_yard_service._operator_precedence("+")
        )
        self.assertEqual(
            2,
            self.shunting_yard_service._operator_precedence("/")
        )
        self.assertEqual(
            2,
            self.shunting_yard_service._operator_precedence("*")
        )

    def test__is_operator_returns_true_if_operator(self):
        self.assertTrue(self.shunting_yard_service._is_operator("-"))
        self.assertTrue(self.shunting_yard_service._is_operator("+"))
        self.assertTrue(self.shunting_yard_service._is_operator("/"))
        self.assertTrue(self.shunting_yard_service._is_operator("*"))

    def test__is_operator_returns_false_if_not_operator(self):
        self.assertFalse(self.shunting_yard_service._is_operator("2"))
        self.assertFalse(self.shunting_yard_service._is_operator("200"))

    def test__is_left_associative_returns_true_if_operator_left_associative(self):
        self.assertTrue(self.shunting_yard_service._is_left_associative("-"))
        self.assertTrue(self.shunting_yard_service._is_left_associative("+"))
        self.assertTrue(self.shunting_yard_service._is_left_associative("/"))
        self.assertTrue(self.shunting_yard_service._is_left_associative("*"))

    def test__is_left_associative_returns_false_if_operator_not_left_associative(self):
        self.assertFalse(self.shunting_yard_service._is_left_associative("^"))

    def test__pop_from_stack_to_queue_pops_operator_to_queue(self):
        self.shunting_yard_service._operator_stack.push("+")
        self.shunting_yard_service._operator_stack.push("-")
        self.shunting_yard_service._pop_from_stack_to_queue()
        from_queue = self.shunting_yard_service._output_queue.get()
        
        self.assertEqual("-", from_queue)
        self.assertEqual("+", self.shunting_yard_service._operator_stack.top_operator())
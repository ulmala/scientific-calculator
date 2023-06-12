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

    def test__pop_from_stack_to_queue_pops_operator_to_queue(self):
        self.shunting_yard_service._operator_stack.push("+")
        self.shunting_yard_service._operator_stack.push("-")
        self.shunting_yard_service._pop_from_stack_to_queue()
        from_queue = self.shunting_yard_service._output_queue.get()

        self.assertEqual("-", from_queue)
        self.assertEqual(
            "+", self.shunting_yard_service._operator_stack.top_operator())

    def test_run_converts_tokens_to_correct_postfix_format_1(self):
        raw_expression = "3+4.2*2/(1-5)^2^3"
        expression = Expression(raw_expression=raw_expression)
        tokens = ["3", "+", "4.2", "*", "2", "/",
                  "(", "1", "-", "5", ")", "^", "2", "^", "3"]
        expression.tokens = tokens
        expression = self.shunting_yard_service.run(expression=expression)
        correct_postfix = ["3", "4.2", "2", "*", "1",
                           "5", "-", "2", "3", "^", "^", "/", "+"]
        self.assertEqual(correct_postfix, expression.postfix)

    def test_run_converts_tokens_to_correct_postfix_format_2(self):
        raw_expression = "sin(max(2,3)/3*3.1)"
        expression = Expression(raw_expression=raw_expression)
        tokens = ["sin", "(", "max", "(", "2", ",", "3", ")",
                  "/", "3", "*", "3.1", ")"]
        expression.tokens = tokens
        expression = self.shunting_yard_service.run(expression=expression)
        correct_postfix = ["2", "3", "max", "3", "/", "3.1", "*", "sin"]
        self.assertEqual(correct_postfix, expression.postfix)

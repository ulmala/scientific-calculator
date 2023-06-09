from entities.expression import Expression
from entities.operator_stack import OperatorStack
from entities.output_queue import OutputQueue

from services.validation_service import (
    validation_service as default_validation_service
)

from config import OPERATOR_PRECEDENCE


class ShuntingYardService:
    """
    Class responsible for executing the Shungting Yard algorithm
    """

    def __init__(
            self,
            validation_service=default_validation_service
    ) -> None:
        self._output_queue = OutputQueue()
        self._operator_stack = OperatorStack()
        self._operator_prec = OPERATOR_PRECEDENCE
        self._validation_service = validation_service

    def _clear_stack_and_queue(self):
        """
        Clears stack and queue before algorithm execution
        """
        self._output_queue = OutputQueue()
        self._operator_stack = OperatorStack()

    def _operator_precedence(
            self,
            token: str
    ) -> int:
        """
        Returns operator precedence

        Args:
            token (str): operator

        Returns:
            int: operator precedence
        """
        return self._operator_prec[token]

    def _pop_from_stack_to_queue(self):
        """
        Pop operator from stack into output queue
        """
        operator = self._operator_stack.pop()
        self._output_queue.put(operator)

    def run(
            self,
            expression: Expression
    ) -> Expression:
        """
        The Shunting Yard algorithm

        Args:
            expression (Expression): expression to be handled

        Returns:
            Expression: expression with postfix notation
        """
        self._clear_stack_and_queue()

        # while there are tokens to be read:
        for token in expression.tokens:
            # if token is a number: put it into the output queue
            if self._validation_service.is_number(token):
                self._output_queue.put(token)

            # if token is a function: push it onto the operator stack
            if self._validation_service.is_function(token):
                self._operator_stack.push(token)

            # if token is an operator:
            elif self._validation_service.is_operator(token):
                # while (
                #   there is an operator o2 at the top of the operator stack
                #   which is not a left parenthesis,
                #   and (o2 has greater precedence than o1 or
                #   (o1 and o2 have the same precedence and o1 is left-associative))
                # ):
                if not self._operator_stack.is_empty():
                    while self._operator_stack.top_operator() != "(" and (
                            self._operator_stack.top_operator_precedence() > self._operator_precedence(token) or
                            (self._operator_stack.top_operator_precedence() == self._operator_precedence(
                                token) and self._validation_service.is_left_associative(token))
                    ):
                        # pop o2 from the operator stack into the output queue
                        self._pop_from_stack_to_queue()
                        if self._operator_stack.is_empty():
                            break

                # push o1 onto the operator stack
                self._operator_stack.push(token)

            # - a left parenthesis (i.e. "("):
            if token == "(":
                # push it onto the operator stack
                self._operator_stack.push(token)

            # - a right parenthesis (i.e. ")"):
            if token == ")":
                # if not self._operator_stack.is_empty():
                # while the operator at the top of the operator stack is not a left parenthesis:
                while self._operator_stack.top_operator() != "(":
                    # pop the operator from the operator stack into the output queue
                    self._pop_from_stack_to_queue()

                # pop the left parenthesis from the operator stack and discard it
                self._operator_stack.pop()

                # if there is a function token at the top of the operator stack, then:
                #   pop the function from the operator stack into the output queue
                if self._operator_stack.function_at_top():
                    self._pop_from_stack_to_queue()

        while not self._operator_stack.is_empty():
            self._pop_from_stack_to_queue()

        expression.postfix = self._output_queue.as_list()
        return expression


shunting_yard_service = ShuntingYardService()

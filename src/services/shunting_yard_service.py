from entities.expression import Expression
from entities.operator_stack import OperatorStack
from entities.output_queue import OutputQueue

from constants import OPERATOR_PRECEDENCE, OPERATORS, LEFT_ASSOCIATIVE_OPERATORS

class ShuntingYardService:
    def __init__(self) -> None:
        self._output_queue = OutputQueue()
        self._operator_stack = OperatorStack()
        self._operator_prec = OPERATOR_PRECEDENCE
        self._operators = OPERATORS
        self._left_associative_operators = LEFT_ASSOCIATIVE_OPERATORS
    
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
    
    def _is_operator(
            self,
            token: str
    ) -> bool:
        """
        Checks if token is an operators

        Args:
            token (str): token to be checked

        Returns:
            bool: True if operator, else False
        """
        if token in self._operators:
            return True
        return False
    
    def _is_left_associative(
            self,
            token: str
    ) -> bool:
        """
        Checks if operator is left associative

        Args:
            token (str): operator to be checked

        Returns:
            bool: True if left associative, else False
        """
        if token in self._left_associative_operators:
            return True
        return False
    
    def _pop_from_stack_to_queue(self):
        """
        Pop operator from stack into output queue
        """
        operator = self._operator_stack.pop()
        self._output_queue.put(operator)

    def _print_status(self, token):
            print("*********** CURRENT STATUS ***********")
            print("stack: ", self._operator_stack)
            print("output queue: ", self._output_queue)
            print("next token to be handled: ", token)
            input()

    def run(
            self,
            expression: Expression
    ) -> Expression:
        tokens = expression.tokens()

        # while there are tokens to be read:
        for token in tokens:
            self._print_status(token)

            # if token is a number: put it into the output queue
            if token.isdigit():
                self._output_queue.put(token)

            # TODO: if token is a function: push it onto the operator stack

            # if token is an operator:
            elif self._is_operator(token):
                # while (
                # there is an operator o2 at the top of the operator stack which is not a left parenthesis, 
                # and (o2 has greater precedence than o1 or (o1 and o2 have the same precedence and o1 is left-associative))
                # ):
                if not self._operator_stack.is_empty():
                    while self._operator_stack.top_operator() != "(" and (
                            self._operator_stack.top_operator_precedence() > self._operator_precedence(token) or
                            (self._operator_stack.top_operator_precedence() == self._operator_precedence(token) and self._is_left_associative(token))
                    ):
                        # pop o2 from the operator stack into the output queue
                        self._pop_from_stack_to_queue()
                        if self._operator_stack.is_empty():
                            break

                # push o1 onto the operator stack
                self._operator_stack.push(token)

            # TODO: # - a ",":
                    #   while the operator at the top of the operator stack is not a left parenthesis:
                    #       pop the operator from the operator stack into the output queue
            
            # - a left parenthesis (i.e. "("):
            if token == "(":
                # push it onto the operator stack
                self._operator_stack.push(token)

            # - a right parenthesis (i.e. ")"):
            if token == ")":
                if not self._operator_stack.is_empty():
                    # while the operator at the top of the operator stack is not a left parenthesis:
                    while self._operator_stack.top_operator() != "(":
                        # TODO: {assert the operator stack is not empty}
                        # /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */

                        # pop the operator from the operator stack into the output queue
                        self._pop_from_stack_to_queue()

                # TODO: {assert there is a left parenthesis at the top of the operator stack}

                # pop the left parenthesis from the operator stack and discard it
                self._operator_stack.pop()

                #TODO: if there is a function token at the top of the operator stack, then:
                        # pop the function from the operator stack into the output queue

        # /* After the while loop, pop the remaining items from the operator stack into the output queue. */
        # while there are tokens on the operator stack:

        # TODO: /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
                # {assert the operator on top of the stack is not a (left) parenthesis}

        while not self._operator_stack.is_empty():
            self._pop_from_stack_to_queue()  

        print("stack:", self._operator_stack)
        print("queue: ", self._output_queue)

        expression.set_postfix_notation(self._output_queue.as_list())
        return expression


shunting_yard_service = ShuntingYardService()

from entities.equation import Equation
from entities.operator_stack import OperatorStack
from entities.output_queue import OutputQueue

class ShutingYard:
    def __init__(self) -> None:
        self._output_queue = OutputQueue()
        self._operator_stack = OperatorStack()
        self._operator_prec = {
            "(": 0,
            "-": 1,
            "+": 1,
            "/": 2,
            "*": 2,
        }

    def _is_operator(
            self,
            token: str
    ) -> bool:
        if token in ["+", "-", "*", "/"]:
            return True
        return False

    def _is_left_associative(
            self,
            token: str
    ) -> bool:
        if token in ["+", "-", "*", "/"]:
            return True
        return False

    def _pop_from_stack_to_queue(self):
        operator = self._operator_stack.pop()
        self._output_queue.put(operator)

    def run(
            self,
            equation: Equation
    ) -> Equation:
        tokens = equation.tokens()
        
        # while there are tokens to be read:
        for token in tokens:

            print("*********** CURRENT STATUS ***********")
            print("stack: ", self._operator_stack)
            print("output queue: ", self._output_queue)
            print("next token to be handled: ", token)
            input()

            # if token is a number: put it into the output queue
            if token.isdigit():
                self._output_queue.put(token)

            # if token is a function: push it onto the operator stack
            # TODO: support for functions

            # if token is an operator:
            elif self._is_operator(token):
                # while (
                # there is an operator o2 at the top of the operator stack which is not a left parenthesis, 
                # and (o2 has greater precedence than o1 or (o1 and o2 have the same precedence and o1 is left-associative))
                # ):
                if not self._operator_stack.is_empty():
                    while self._operator_stack.top_operator() != "(" and (
                            self._operator_stack.top_operator_precedence() > self._operator_prec[token] or
                            (self._operator_stack.top_operator_precedence() == self._operator_prec[token] and self._is_left_associative(token))
                    ):
                        # pop o2 from the operator stack into the output queue
                        print(token, self._operator_stack)
                        self._pop_from_stack_to_queue()
                        print(token, self._operator_stack)
                        if self._operator_stack.is_empty():
                            break
                # push o1 onto the operator stack
                self._operator_stack.push(token)

            # - a ",":
            #   while the operator at the top of the operator stack is not a left parenthesis:
            #       pop the operator from the operator stack into the output queue
            # TODO: implement this

            # - a left parenthesis (i.e. "("):
            if token == "(":
                # push it onto the operator stack
                self._operator_stack.push(token)

            # - a right parenthesis (i.e. ")"):
            if token == ")":
                if not self._operator_stack.is_empty():
                    # while the operator at the top of the operator stack is not a left parenthesis:
                    while self._operator_stack.top_operator() != "(":
                        # TODO: implement this:
                        # {assert the operator stack is not empty}
                        # /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */

                        # pop the operator from the operator stack into the output queue
                        self._pop_from_stack_to_queue()

                # TODO: implement validation
                # {assert there is a left parenthesis at the top of the operator stack}
                print(self._operator_stack)

                # pop the left parenthesis from the operator stack and discard it
                self._operator_stack.pop()
                print(self._operator_stack)

                #TODO:
                # if there is a function token at the top of the operator stack, then:
                    # pop the function from the operator stack into the output queue

        # /* After the while loop, pop the remaining items from the operator stack into the output queue. */
        # while there are tokens on the operator stack:

        # TODO:
        # /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
        # {assert the operator on top of the stack is not a (left) parenthesis}

        while not self._operator_stack.is_empty():
            self._pop_from_stack_to_queue()            

        print("stack:", self._operator_stack)
        print("queue: ", self._output_queue)


            

                
            


shunting_yard = ShutingYard()

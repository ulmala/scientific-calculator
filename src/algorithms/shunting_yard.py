import queue
from entities.equation import Equation

class ShutingYard:
    def __init__(self) -> None:
        self._output_queue = queue.Queue()
        self._operator_stack = []
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

# while there are tokens to be read:
#     read a token
#     if the token is:
#     - a number:
#         put it into the output queue
#     - a function:
#         push it onto the operator stack 
#     - an operator o1:
#         while (
#             there is an operator o2 at the top of the operator stack which is not a left parenthesis, 
#             and (o2 has greater precedence than o1 or (o1 and o2 have the same precedence and o1 is left-associative))
#         ):
#             pop o2 from the operator stack into the output queue
#         push o1 onto the operator stack
#     - a ",":
#         while the operator at the top of the operator stack is not a left parenthesis:
#              pop the operator from the operator stack into the output queue
#     - a left parenthesis (i.e. "("):
#         push it onto the operator stack
#     - a right parenthesis (i.e. ")"):
#         while the operator at the top of the operator stack is not a left parenthesis:
#             {assert the operator stack is not empty}
#             /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */
#             pop the operator from the operator stack into the output queue
#         {assert there is a left parenthesis at the top of the operator stack}
#         pop the left parenthesis from the operator stack and discard it
#         if there is a function token at the top of the operator stack, then:
#             pop the function from the operator stack into the output queue
# /* After the while loop, pop the remaining items from the operator stack into the output queue. */
# while there are tokens on the operator stack:
#     /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
#     {assert the operator on top of the stack is not a (left) parenthesis}
#     pop the operator from the operator stack onto the output queue

    def run(
            self,
            equation: Equation
    ) -> Equation:
        tokens = equation.tokens()
        
        # while there are tokens to be read:
        for token in tokens:

            print("*********** CURRENT STATUS ***********")
            print("stack: ", self._operator_stack)
            print("output queue: ", list(self._output_queue.queue))
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
                if len(self._operator_stack) > 0:
                    while (self._operator_stack[-1] != "(") \
                        and ((self._operator_prec[self._operator_stack[-1]] > self._operator_prec[token]) \
                            or ( (self._operator_prec[self._operator_stack[-1]] == self._operator_prec[token] ) and self._is_left_associative(token))):
                        # pop o2 from the operator stack into the output queue
                        print(token, self._operator_stack)
                        self._output_queue.put(self._operator_stack.pop())
                        print(token, self._operator_stack)
                        if len(self._operator_stack) == 0:
                            break
                # push o1 onto the operator stack
                self._operator_stack.append(token)

            # - a ",":
            #   while the operator at the top of the operator stack is not a left parenthesis:
            #       pop the operator from the operator stack into the output queue
            # TODO: implement this

            # - a left parenthesis (i.e. "("):
            if token == "(":
                # push it onto the operator stack
                self._operator_stack.append(token)

            # - a right parenthesis (i.e. ")"):
            if token == ")":
                if len(self._operator_stack) > 0:
                    # while the operator at the top of the operator stack is not a left parenthesis:
                    while self._operator_stack[-1] != "(":
                        # TODO: implement this:
                        # {assert the operator stack is not empty}
                        # /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */

                        # pop the operator from the operator stack into the output queue
                        self._output_queue.put(self._operator_stack.pop())

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

        while len(self._operator_stack) > 0:
            self._output_queue.put(self._operator_stack.pop())            

        print("stack:", self._operator_stack)
        print("queue: ", list(self._output_queue.queue))


            

                
            


shunting_yard = ShutingYard()

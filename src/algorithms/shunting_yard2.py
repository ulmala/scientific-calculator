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

    def run(
            self,
            equation: Equation
    ) -> Equation:
        tokens = equation.tokens()
        for token in tokens:
            if token.isdigit():
                self._output_queue.put(token)

#    - an operator o1:
#        while (
#            there is an operator o2 at the top of the operator stack which is not a left parenthesis, 
#            and (o2 has greater precedence than o1 or (o1 and o2 have the same precedence and o1 is left-associative))
#        ):
#            pop o2 from the operator stack into the output queue
#        push o1 onto the operator stack

            elif self._is_operator(token):

                if len(self._operator_stack) > 0:

                    while (self._operator_stack[-1] == "(") \
                        and ((self._operator_prec[self._operator_stack[-1]] > self._operator_prec[token]) \
                            or ( (self._operator_prec[self._operator_stack[-1]] == self._operator_prec[token] ) and self._is_left_associative(token))):
                        self._output_queue.put(self._operator_stack.pop())
                self._operator_stack.append(token)
            

            elif token == "(":
                self._operator_stack.append(token)

            elif token == ")": # - a right parenthesis (i.e. ")"):
                if len(self._operator_stack) > 0:
                    while (self._operator_stack[-1] != "("): #while the operator at the top of the operator stack is not a left parenthesis:
                        self._output_queue.put(self._operator_stack.pop()) # pop the operator from the operator stack into the output queue

                    print(self._operator_stack[-1])
                    print("LOL")

            # - a right parenthesis (i.e. ")"):
                # while the operator at the top of the operator stack is not a left parenthesis:
                    # {assert the operator stack is not empty}
                    # /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */
                    # pop the operator from the operator stack into the output queue
                # {assert there is a left parenthesis at the top of the operator stack}
                # pop the left parenthesis from the operator stack and discard it
                # if there is a function token at the top of the operator stack, then:
                    # pop the function from the operator stack into the output queue


        #while there are tokens on the operator stack:
        #    /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
        #    {assert the operator on top of the stack is not a (left) parenthesis}
        #    pop the operator from the operator stack onto the output queue
        while len(self._operator_stack) > 0:
            self._output_queue.put(self._operator_stack.pop())

        print(list(self._output_queue.queue))


shunting_yard = ShutingYard()

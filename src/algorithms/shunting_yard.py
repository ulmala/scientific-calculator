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

#1.  While there are tokens to be read:
#2.        Read a token
#3.        If it's a number add it to queue
#4.        If it's an operator
#5.               While there's an operator on the top of the stack with greater precedence:
#6.                       Pop operators from the stack onto the output queue
#7.               Push the current operator onto the stack
#8.        If it's a left bracket push it onto the stack
#9.        If it's a right bracket 
#10.            While there's not a left bracket at the top of the stack:
#11.                     Pop operators from the stack onto the output queue.
#12.             Pop the left bracket from the stack and discard it
#13. While there are operators on the stack, pop them to the queue

        for token in tokens:
            #3. If it's a number add it to queue
            if token.isdigit():
                self._output_queue.put(token)

            #4. If it's an operator
            elif self._is_operator(token):
                if len(self._operator_stack) > 0:
                    #5. While there's an operator on the top of the stack with greater precedence:
                    while self._operator_prec[self._operator_stack[-1]] > self._operator_prec[token]:
                        #6. Pop operators from the stack onto the output queue
                        self._output_queue.put(self._operator_stack.pop())
                    #7. Push the current operator onto the stack
                    self._operator_stack.append(token)
            #8. If it's a left bracket push it onto the stack
            elif token == "(":
                self._operator_stack.append(token)
            #9. If it's a right bracket
            elif token == ")":
                #10. While there's not a left bracket at the top of the stack:
                while self._operator_stack[-1] != ")":
                    #11. Pop operators from the stack onto the output queue.
                    self._output_queue.put(self._operator_stack.pop())
                #12. Pop the left bracket from the stack and discard it
                self._operator_stack.pop()
        #13. While there are operators on the stack, pop them to the queue
        while len(self._operator_stack) > 0:
            self._output_queue.put(self._operator_stack.pop())

        print("stack:", self._operator_stack)
        print("queue: ", list(self._output_queue.queue))


            

                
            


shunting_yard = ShutingYard()

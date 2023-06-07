from constants import (
    OPERATOR_PRECEDENCE,
    OPERATORS,
    SUPPORTED_FUNCTIONS
)


class OperatorStack:
    """
    Operator stack used in Shungting Yard algorithm
    """

    def __init__(self) -> None:
        """
        Class constructor
        """
        self._stack = []
        self._operator_prec = OPERATOR_PRECEDENCE
        self._operators = OPERATORS
        self._supported_functions = SUPPORTED_FUNCTIONS

    def __str__(self) -> str:
        """
        Returns the stack as string

        Returns:
            str: stack
        """
        return str(self._stack)

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if empty, else False
        """
        if len(self._stack) > 0:
            return False
        return True

    def top_operator(self) -> str:
        """
        Returns the operator at top of the stack 
        (doesn't pop the value from stack).

        Returns:
            str: operator
        """
        return self._stack[-1]

    def top_operator_precedence(self) -> int:
        """
        Returns the operator's precedence which is at
        the top of the stack

        Returns:
            int: operator precedence
        """
        return self._operator_prec[self.top_operator()]

    def push(
            self,
            token: str
    ):
        """
        Pushes token to the stack

        Args:
            token (str): token to be pushed
        """
        self._stack.append(token)

    def pop(self) -> str:
        """
        Pops value from the stack if the stack
        is not empty. Else returns None

        Returns:
            str: popped value
        """
        if self.is_empty():
            return None
        return self._stack.pop()

    def function_at_top(self) -> bool:
        """
        Checks if the stack's top toke is a function

        Returns:
            bool: True if function, else False
        """
        if self.top_operator() in self._supported_functions:
            return True
        return False

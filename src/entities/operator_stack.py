from constants import OPERATOR_PRECEDENCE, OPERATORS

class OperatorStack:
    def __init__(self) -> None:
        self._stack = []
        self._operator_prec = OPERATOR_PRECEDENCE
        self._operators = OPERATORS

    def __str__(self) -> str:
        return str(self._stack)

    def is_empty(self) -> bool:
        if len(self._stack) > 0:
            return False
        return True
    
    def top_operator(self) -> str:
        return self._stack[-1]
    
    def top_operator_precedence(self) -> int:
        return self._operator_prec[self.top_operator()]
    
    def operator_at_top(self) -> bool:
        if self._stack[-1] in self._operators:
            return True
        return False
    
    def push(
            self,
            token: str
    ):
        self._stack.append(token)

    def pop(self) -> str:
        if self.is_empty():
            return None
        return self._stack.pop()
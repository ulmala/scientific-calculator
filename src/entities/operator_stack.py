class OperatorStack:
    def __init__(self) -> None:
        self._stack = []

    def is_empty(self):
        if len(self._stack) > 0:
            return False
        return True
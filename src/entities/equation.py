class Equation:
    def __init__(
            self,
            raw_equation
    ) -> None:
        self._raw_equation = raw_equation
        self._tokens = []

    def raw_equation(self) -> str:
        return self._raw_equation
    
    def tokens(self) -> list:
        return self._tokens

    def set_tokens(
            self,
            tokens: list
    ):
        self._tokens = tokens
    
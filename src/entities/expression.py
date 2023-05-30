class Expression:
    def __init__(
            self,
            raw_expression
    ) -> None:
        self._raw_expression = raw_expression
        self._tokens = []

    def raw_expression(self) -> str:
        return self._raw_expression
    
    def tokens(self) -> list:
        return self._tokens

    def set_tokens(
            self,
            tokens: list
    ):
        self._tokens = tokens
    
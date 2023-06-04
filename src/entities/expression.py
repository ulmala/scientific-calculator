class Expression:
    def __init__(
            self,
            raw_expression
    ) -> None:
        self._raw_expression = raw_expression
        self._tokens = []
        self._postfix_notation = None
        self._value = None

    def __str__(self) -> str:
        raw_expression = f"raw expression: {self._raw_expression}"
        tokens = f"tokens: {self._tokens}"
        postfix = f"postfix notation: {self._postfix_notation}"
        return f"{raw_expression}\n{tokens}\n{postfix}"

    def raw_expression(self) -> str:
        return self._raw_expression
    
    def tokens(self) -> list:
        return self._tokens

    def set_tokens(
            self,
            tokens: list
    ):
        self._tokens = tokens

    def set_postfix(
            self,
            notation: list
    ):
        self._postfix_notation = notation
    
    def postfix(self) -> list:
        return self._postfix_notation
    
    def set_value(
            self,
            value
    ):
        self._value = value
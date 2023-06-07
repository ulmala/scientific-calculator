class Expression:
    """
    Class to hold information of the experssion and it's
    different forms.
    """

    def __init__(
            self,
            raw_expression: str
    ) -> None:
        """
        Class constructor

        Args:
            raw_expression (str): expression in raw string format
        """
        self._raw_expression = raw_expression
        self._tokens = []
        self._postfix_notation = None
        self._value = None

    def __str__(self) -> str:
        """String representation of the object"""
        raw_expression = f"raw expression: {self._raw_expression}"
        tokens = f"tokens: {self._tokens}"
        postfix = f"postfix notation: {self._postfix_notation}"
        return f"{raw_expression}\n{tokens}\n{postfix}"

    def raw_expression(self) -> str:
        """
        Returns raw expression as string

        Returns:
            str: raw expression
        """
        return self._raw_expression

    def tokens(self) -> list:
        """
        Returns expression tokens as list

        Returns:
            list: tokens
        """
        return self._tokens

    def set_tokens(
            self,
            tokens: list
    ):
        """
        Sets tokens to class variable.

        Args:
            tokens (list): tokens
        """
        self._tokens = tokens

    def set_postfix(
            self,
            notation: list
    ):
        """
        Sets postfix notation of the expression to
        class variable

        Args:
            notation (list): postfix notation
        """
        self._postfix_notation = notation

    def postfix(self) -> list:
        """
        Returns expression's postfix notation as list

        Returns:
            list: postfix notation
        """
        return self._postfix_notation

    def set_value(
            self,
            value: float
    ):
        """
        Sets the value of solved expression
        into class variable

        Args:
            value (float): value of solved expression
        """
        self._value = value

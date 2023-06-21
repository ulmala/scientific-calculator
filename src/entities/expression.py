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
        return f"{' '.join(self._tokens)} = {self._value}"

    @property
    def raw_expression(self) -> str:
        """
        Returns raw expression as string

        Returns:
            str: raw expression
        """
        return self._raw_expression

    @raw_expression.setter
    def raw_expression(
        self,
        raw_expression: str
    ):
        """
        Sets raw expression to class variable

        Args:
            raw_expression (str): raw expression
        """
        self._raw_expression = raw_expression

    @property
    def tokens(self) -> list:
        """
        Returns expression tokens as list

        Returns:
            list: tokens
        """
        return self._tokens

    @tokens.setter
    def tokens(
            self,
            tokens: list
    ):
        """
        Sets tokens to class variable

        Args:
            tokens (list): tokens
        """
        self._tokens = tokens

    @property
    def postfix(self) -> list:
        """
        Returns expression's postfix notation as list

        Returns:
            list: postfix notation
        """
        return self._postfix_notation

    @postfix.setter
    def postfix(
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

    @property
    def value(self) -> float:
        """
        Value of solved expression

        Returns:
            float: value of experssion
        """
        return self._value

    @value.setter
    def value(
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

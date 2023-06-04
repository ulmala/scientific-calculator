import re
from entities.expression import Expression


class ParserService:
    """
    Responsible for parsing and validatig expressions
    """

    def __init__(self):
        self._validations = [
            self._expression_starts_with_valid_token
        ]

    def _expression_starts_with_digit(
            self,
            expression: Expression
    ) -> bool:
        """
        Check if the expression starts with a digit.

        Args:
            expression (Expression): expression object validate

        Returns:
            bool: True if starts with digit, else False
        """
        if not expression.raw_expression()[0].isdigit():
            return False
        return True

    def _expression_starts_with_left_paranthesis(
            self,
            expression: Expression
    ) -> bool:
        """
        Check if expressions starts with left paranthesis

        Args:
            expression (Expression): expression object validate

        Returns:
            bool: True if starts with '(' , else False
        """
        if expression.raw_expression()[0] == "(":
            return True
        return False

    def _expression_starts_with_valid_token(
            self,
            expression: Expression
    ) -> bool:
        """
        Check if expressions starts with valid token

        Args:
            expression (Expression): expression object to validate

        Returns:
            bool: True if valid token, else False
        """
        if self._expression_starts_with_digit(expression):
            return True
        if self._expression_starts_with_left_paranthesis(expression):
            return True
        return False

    def validate_expression(
            self,
            expression: Expression
    ) -> bool:
        """
        Runs all expression validations.

        Args:
            expression (Expression): expression object validate

        Returns:
            bool: True if valid expression, else False
        """
        for validation in self._validations:
            if not validation(expression):
                return False
        return True

    def parse_to_tokens(
            self,
            expression: Expression
    ) -> Expression:
        """
        Parse raw expression into list of tokens. Updates expression 
        object and returns it.

        Args:
            expression (Expression): expression object with no tokens

        Returns:
            Expression: expression object with tokens
        """
        tokens = re.findall(r"\d+|\S", expression.raw_expression())
        expression.set_tokens(tokens)
        return expression


parser_service = ParserService()

import re
from entities.expression import Expression
from constants import (
    SUPPORTED_FUNCTIONS
)


class ParserService:
    """
    Responsible for parsing and validatig expressions
    """

    def __init__(self):
        self._validations = [
            self._expression_starts_with_valid_token
        ]

    def is_valid_variable_name(
            self,
            variable_name: str
    ) -> bool:
        if variable_name.isalpha() and \
                variable_name not in SUPPORTED_FUNCTIONS:
            return True
        return False

    def is_number(
            self,
            token: str
    ) -> bool:
        try:
            float(token)
            return True
        except:
            return False

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
        # if self._expression_starts_with_digit(expression):
        #     return True
        # if self._expression_starts_with_left_paranthesis(expression):
        #     return True
        # if self._expression_starts_with_function(expression):
        #     return True
        # return False
        return True

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

    def _get_escaped_funcs_and_vars(
            self,
            variables: dict
    ) -> list:
        funcs_and_vars = list(SUPPORTED_FUNCTIONS.keys()
                              ) + list(variables.keys())
        escaped_funcs_and_vars = [
            re.escape(substring) for substring in funcs_and_vars]
        return escaped_funcs_and_vars

    def _convert_variables_to_values(
            self,
            tokens: list,
            variables: dict
    ) -> list:
        for i in range(len(tokens)):
            if tokens[i] in variables:
                tokens[i] = variables[tokens[i]]
        return tokens

    def parse_to_tokens(
            self,
            expression: Expression,
            variables: dict
    ) -> Expression:
        """
        Parse raw expression into list of tokens. Updates expression 
        object and returns it.

        Args:
            expression (Expression): expression object with no tokens

        Returns:
            Expression: expression object with tokens
        """
        escaped_funcs_and_vars = self._get_escaped_funcs_and_vars(variables)
        pattern = r"(\d+(?:\.\d+)?|\+|\-|\*|\^|\/|\(|\)|\,|" + \
            "|".join(escaped_funcs_and_vars) + ")"
        tokens = re.findall(pattern, expression.raw_expression())
        tokens = self._convert_variables_to_values(tokens, variables)
        expression.set_tokens(tokens)
        return expression


parser_service = ParserService()

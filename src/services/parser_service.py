import re
from entities.expression import Expression
from services.validation_service import (
    validation_service as default_validation_service
)
from config import (
    SUPPORTED_FUNCTIONS
)


class ParserService:
    """
    Responsible for parsing and validatig expressions
    """

    def __init__(
            self,
            validation_service=default_validation_service
    ) -> None:
        self._validation_service = validation_service

    def _get_escaped_funcs_and_vars(
            self,
            variables: dict
    ) -> list:
        """
        Returns list of escaped function names and 
        variables

        Args:
            variables (dict): user defined variables

        Returns:
            list: list of escaped functions and variables
        """
        funcs_and_vars = list(SUPPORTED_FUNCTIONS.keys())\
            + list(variables.keys())
        escaped_funcs_and_vars = [
            re.escape(substring) for substring in funcs_and_vars
        ]
        return escaped_funcs_and_vars

    def _convert_variables_to_values(
            self,
            tokens: list,
            variables: dict
    ) -> list:
        """
        Convert variable names to their values in tokens.
        E.g. ['a', '+', '1'] -> ['2', '+', '1']

        Args:
            tokens (list): list of tokens
            variables (dict): user defined variables

        Returns:
            list: tokens where variables converted to values
        """
        for i, token in enumerate(tokens):
            if token in variables:
                tokens[i] = variables[token]
        return tokens

    def _remove_whitespaces(
            self,
            expression: Expression
    ) -> Expression:
        """
        Remove all whitespaces from the user given
        raw expression

        Args:
            expression (Expression): expression object

        Returns:
            Expression: expression object
        """
        expression.raw_expression = expression.raw_expression.replace(" ", "")
        return expression

    def _add_leading_zero_if_starting_with_minus(
            self,
            expression: Expression
    ) -> Expression:
        """
        If user's expression starts with '-' this method will add
        leading zero to the expression. This way the Shuting Yard
        algorithm will handle expression correctly

        Args:
            expression (Expression): expression to be checked

        Returns:
            Expression: modified expression
        """
        if expression.raw_expression[0] == "-":
            expression.raw_expression = "0" + expression.raw_expression
        return expression

    def _get_tokens(
            self,
            expression: Expression,
            variables: dict
    ) -> list:
        """
        Parse expression in to tokens;
        all arithmetic operators, number, functions etc.

        Args:
            expression (Expression): expression to be handled
            variables (dict): user defined variables

        Returns:
            list: list of tokens
        """
        escaped_funcs_and_vars = self._get_escaped_funcs_and_vars(variables)
        pattern = r"(\d+(?:\.\d+)?|\+|\-|\*|\^|\/|\(|\)|\,|" + \
            "|".join(escaped_funcs_and_vars) + ")"
        tokens = re.findall(pattern, expression.raw_expression)
        return tokens

    def _replace_negative_exponent_by_alternative_form(
            self,
            expression: Expression
    ) -> Expression:
        """
        Converts negative exponent into alternative form, e.g.
        2^(-3) --> 1/(2^3). This prevents the postfix notation
        evaluation to break.

        Args:
            expression (Expression): expression to be handled

        Returns:
            Expression: modified expression
        """
        pattern = r"(\d+)\^\((-\d+)\)"
        matches = re.findall(pattern, expression.raw_expression)
        for base, exponent in matches:
            replacement = f"1/({base}^{abs(float(exponent))})"
            expression.raw_expression = expression.raw_expression.replace(
                f'{base}^({exponent})', replacement)
        return expression

    def parse_to_tokens(
            self,
            expression: Expression,
            variables: dict
    ) -> Expression:
        """
        This is the 'main' function when parsings expression to tokens.
        Executes following:
        - removes whitespaces
        - adds leading zero to the epxression if starting with zero
        - converts negative exponent into alternative form
        - parse raw epxression in to list of tokens
        - validates that no tokens were dropped in parsing
        - converts all varibales into numeric values
        - sets tokens to the Expression object

        Args:
            expression (Expression): Expression object with no tokens

        Returns:
            Expression: Expression object with tokens
        """
        expression = self._remove_whitespaces(expression)
        expression = self._add_leading_zero_if_starting_with_minus(expression)
        expression = self._replace_negative_exponent_by_alternative_form(
            expression)
        tokens = self._get_tokens(expression, variables)
        self._validation_service.check_if_tokens_are_not_dropped(
            tokens, expression
        )
        tokens = self._convert_variables_to_values(tokens, variables)
        expression.tokens = tokens
        return expression


parser_service = ParserService()

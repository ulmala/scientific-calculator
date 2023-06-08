import re
from entities.expression import Expression
from config import (
    SUPPORTED_FUNCTIONS
)


class ParserService:
    """
    Responsible for parsing and validatig expressions
    """
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

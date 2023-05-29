"""Responsible for parsing and validatig equations"""
import re
from entities.equation import Equation


class ParserService:
    """
    Responsible for parsing and validatig equations
    """
    def __init__(self):
        self._validations = [
            self._equation_starts_with_valid_token
        ]

    def _equation_starts_with_digit(
            self,
            equation: Equation
    ) -> bool:
        """
        Check if the equation starts with a digit.

        Args:
            equation (Equation): equation object validate

        Returns:
            bool: True if starts with digit, else False
        """
        if not equation.raw_equation()[0].isdigit():
            return False
        return True

    def _equation_starts_with_left_paranthesis(
            self,
            equation: Equation
    ) -> bool:
        """
        Check if equations starts with left paranthesis

        Args:
            equation (Equation): equation object validate

        Returns:
            bool: True if starts with '(' , else False
        """
        if equation.raw_equation()[0] == "(":
            return True
        return False

    def _equation_starts_with_valid_token(
            self,
            equation: Equation
    ) -> bool:
        """
        Check if equations starts with valid token

        Args:
            equation (Equation): equation object to validate

        Returns:
            bool: True if valid token, else False
        """
        if self._equation_starts_with_digit(equation):
            return True
        if self._equation_starts_with_left_paranthesis(equation):
            return True
        return False

    def validate_equation(
            self,
            equation: Equation
    ) -> bool:
        """
        Runs all equation validations.
        
        Args:
            equation (Equation): equation object validate

        Returns:
            bool: True if valid equation, else False
        """
        for validation in self._validations:
            if not validation(equation):
                return False
        return True

    def parse_to_tokens(
            self,
            equation: Equation
    ) -> Equation:
        """
        Parse raw equation into list of tokens. Updates equation 
        object and returns it.

        Args:
            equation (Equation): equation object with no tokens

        Returns:
            Equation: equation object with tokens
        """
        pattern = r"([\+\-\%\*])"
        tokens = re.split(pattern, equation.raw_equation())
        equation.set_tokens(tokens)
        return equation

parser_service = ParserService()

import re
from entities.equation import Equation


class ParserService:
    def __init__(self):
        self._validations = [
            self._equation_starts_with_digit
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
        pattern = r"([\=\+\-\%\*])"
        tokens = re.split(pattern, equation.raw_equation())
        equation.set_tokens(tokens)
        return equation
        
    
parser_service = ParserService()

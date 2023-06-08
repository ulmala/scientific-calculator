import re
from entities.expression import Expression
from config import (
    SUPPORTED_FUNCTIONS,
    ONE_PARAMETER_FUNCTIONS,
    TWO_PARAMETER_FUNCTIONS,
    OPERATORS,
    LEFT_ASSOCIATIVE_OPERATORS
)


class NotValidExpression(Exception):
    pass


class ValidationService:
    def __init__(
            self,
            supported_functions=SUPPORTED_FUNCTIONS,
            one_parameter_functions=ONE_PARAMETER_FUNCTIONS,
            two_parameter_functions=TWO_PARAMETER_FUNCTIONS,
            operators=OPERATORS,
            left_associative_operators=LEFT_ASSOCIATIVE_OPERATORS
    ) -> None:
        self._supported_functions = supported_functions
        self._one_parameter_functions = one_parameter_functions
        self._two_parameter_functions = two_parameter_functions
        self._operators = operators
        self._left_associative_operators = left_associative_operators

    def is_number(
            self,
            token: str
    ) -> bool:
        """
        Checks if given token is number

        Args:
            token (str): token to be validated

        Returns:
            bool: True if number, else False
        """
        try:
            float(token)
            return True
        except:
            return False

    def is_function(
            self,
            token: str
    ) -> bool:
        """
        Checks if token is a supported function

        Args:
            token (str): token to be checked

        Returns:
            bool: True if supported operator, else False
        """
        if token in self._supported_functions:
            return True
        return False

    def is_one_parameter_function(
            self,
            token: str
    ) -> bool:
        """
        Checks if the function is one parameter function.

        Args:
            token (str): token to be validated

        Returns:
            bool: True if one parameter function, else False
        """
        if token in self._one_parameter_functions:
            return True
        return False

    def is_two_parameter_function(
            self,
            token: str
    ) -> bool:
        """
        Checks if the function is two parameter function.

        Args:
            token (str): token to be validated

        Returns:
            bool: True if two parameter function, else False
        """
        if token in self._two_parameter_functions:
            return True
        return False

    def is_valid_variable_name(
            self,
            variable_name: str
    ) -> bool:
        if variable_name.isalpha() and \
                variable_name not in self._supported_functions:
            return True
        return False

    def _expression_starts_with_number(
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
        if not self.is_number(expression.raw_expression()[0]):
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

    def _expression_starts_with_alphabet(
            self,
            expression: Expression
    ) -> bool:
        """
        Checks if raw expression starts with alphabet

        Args:
            expression (Expression): expression to be checked

        Returns:
            bool: True if starts with alphabet, else False
        """
        if expression.raw_expression()[0].isalpha():
            return True
        return False

    def _expression_starts_with_plus_or_minus(
            self,
            expression: Expression
    ) -> bool:
        if expression.raw_expression()[0] in ["+", "-"]:
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
        validations = [
            self._expression_starts_with_number,
            self._expression_starts_with_left_paranthesis,
            self._expression_starts_with_alphabet,
            self._expression_starts_with_plus_or_minus
        ]
        if all(validation(expression) == False for validation in validations):
            raise NotValidExpression("Expression starts with illegal token!")

    def _matching_parantheses(
            self,
            expression: Expression
    ):
        """
        Checks if expression has same amount of left and
        right parantheses.

        Args:
            expression (Expression): expression to be validated

        Raises:
            NotValidExpression: if mismatching parantheses
        """
        left_parantheses = len(re.findall(r"\(", expression.raw_expression()))
        right_parantheses = len(re.findall(r"\)", expression.raw_expression()))
        if left_parantheses != right_parantheses:
            raise NotValidExpression("Wrong amount of parantheses!")

    def validate_expression(
            self,
            expression: Expression
    ):
        """
        Runs all validations.

        TODO: validate that expression does not contain undefined variables
        Args:
            expression (Expression): expression to be validated
        """
        self._matching_parantheses(expression)
        self._expression_starts_with_valid_token(expression)

    def is_operator(
            self,
            token: str
    ) -> bool:
        """
        Checks if token is an operators

        Args:
            token (str): token to be checked

        Returns:
            bool: True if operator, else False
        """
        if token in self._operators:
            return True
        return False

    def is_left_associative(
            self,
            token: str
    ) -> bool:
        """
        Checks if operator is left associative

        Args:
            token (str): operator to be checked

        Returns:
            bool: True if left associative, else False
        """
        if token in self._left_associative_operators:
            return True
        return False


validation_service = ValidationService()

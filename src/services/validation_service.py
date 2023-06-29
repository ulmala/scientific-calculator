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
    """Exception raised for invalid expressions"""
    pass


class ValidationService:
    """
    Responsible for offering various validation services
    """
    def __init__(self) -> None:
        self._supported_functions = SUPPORTED_FUNCTIONS
        self._one_parameter_functions = ONE_PARAMETER_FUNCTIONS
        self._two_parameter_functions = TWO_PARAMETER_FUNCTIONS
        self._operators = OPERATORS
        self._left_associative_operators = LEFT_ASSOCIATIVE_OPERATORS

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
        except ValueError:
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
        """
        Checks if given string is valid variable name;
        variable name must be a single alphabet

        Args:
            variable_name (str): variable name to be checked

        Returns:
            bool: True if valid, else False
        """
        if variable_name.isalpha() and \
                variable_name not in self._supported_functions and \
                len(variable_name) == 1:
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
        if not self.is_number(expression.raw_expression[0]):
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
        if expression.raw_expression[0] == "(":
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
        if expression.raw_expression[0].isalpha():
            return True
        return False

    def _expression_starts_with_minus(
            self,
            expression: Expression
    ) -> bool:
        """
        Checks if expression starts with '-' sign

        Args:
            expression (Expression): expression to be checked

        Returns:
            bool: True if starts with '-', else False
        """
        if expression.raw_expression[0] == "-":
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
            self._expression_starts_with_minus
        ]
        if all(validation(expression) is False for validation in validations):
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
        left_parantheses = len(re.findall(r"\(", expression.raw_expression))
        right_parantheses = len(re.findall(r"\)", expression.raw_expression))
        if left_parantheses != right_parantheses:
            raise NotValidExpression("Wrong amount of parantheses!")

    def _expression_is_not_empty(
            self,
            expression: Expression
    ):
        """
        Checks if user given raw expression is empty string

        Args:
            expression (Expression): expression to be checked

        Raises:
            NotValidExpression: if empty string
        """
        if len(expression.raw_expression) == 0:
            raise NotValidExpression("Expression can't be empty!")

    def _correct_power_operator(
            self,
            expression: Expression
    ):
        """
        Checks if user used '**' as power operator,
        valid one is '^'

        Args:
            expression (Expression): expression to be checked

        Raises:
            NotValidExpression: if expression contains '**'
        """
        if "**" in expression.raw_expression:
            raise NotValidExpression(
                "'**' is not a valid power operator! Use '^' instead"
            )

    def _check_if_no_consecutive_operators(
            self,
            expression: Expression
    ):
        """
        Checks if expression contains consecutive operators,
        e.g. '1++1' or '3^^2'

        Args:
            expression (Expression): expression to be checked

        Raises:
            NotValidExpression: if expression contains consecutive operators
        """
        pattern = r"(?:\+\+|--|\*\*|//|[+\-*/]){2,}"
        if re.search(pattern, expression.raw_expression):
            raise NotValidExpression(
                "Consecutive operators are illegal!"
            )
        
    def _expression_ends_with_valid_token(
            self,
            expression: Expression
    ):
        """
        Checks if expression ends with valid token

        Args:
            expression (Expression): expression to be checked

        Raises:
            NotValidExpression: if expression ends with invalid token
        """
        last_token = expression.raw_expression[-1]
        if self.is_operator(last_token):
            raise NotValidExpression(
                "Expression ends with invalid token"
            )

    def validate_expression(
            self,
            expression: Expression
    ):
        """
        Runs all expression validations, checks if:
        - expression is empty
        - correct power operator is used
        - consecutive operators exists
        - parantheses match
        - expression starts with valid token

        Args:
            expression (Expression): expression to be validated
        """
        self._expression_is_not_empty(expression)
        self._correct_power_operator(expression)
        self._check_if_no_consecutive_operators(expression)
        self._matching_parantheses(expression)
        self._expression_starts_with_valid_token(expression)
        self._expression_ends_with_valid_token(expression)

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

    def check_if_tokens_are_not_dropped(
            self,
            tokens: list,
            expression: Expression
    ):
        """
        Validates that parsed tokens has the same length as
        the raw expression, ergo tokens were parsed correctly.

        Args:
            tokens (list): list of tokens
            expression (Expression): expression

        Raises:
            NotValidExpression: if raw_expression and token len are not equal
        """
        if len(expression.raw_expression) != len("".join(tokens)):
            raise NotValidExpression("Not a valid expression!")


validation_service = ValidationService()

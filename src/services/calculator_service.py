from entities.expression import Expression
from services.shunting_yard_service import (
    shunting_yard_service as default_shunting_yard_service
)
from services.validation_service import (
    validation_service as default_validation_service
)
from services.parser_service import (
    parser_service as default_parser_service
)

from config import (
    SUPPORTED_FUNCTIONS
)


class CalculatorService:
    """
    Responsible for executing the high level calculation logic
    """

    def __init__(
            self,
            shunting_yard_service=default_shunting_yard_service,
            validation_service=default_validation_service,
            parser_service=default_parser_service
    ) -> None:
        """
        Class constructor

        Args:
            shunting_yard_service (ShuntingYardService): Defaults to default_shunting_yard_service.
        """
        self._shunting_yard_service = shunting_yard_service
        self._validation_service = validation_service
        self._parser_service = parser_service
        self._variables = {}

    def add_variable(
            self,
            variable_name: str,
            variable_value: str
    ):
        self._variables[variable_name] = variable_value

    def variables(self) -> dict:
        return self._variables

    def print_variables(self):
        for var_name, var_value in self._variables.items():
            print(f"{var_name} = {var_value}")

    def solve(
            self,
            expression: Expression
    ):
        """
        Solves the expression by:
        - converting the expression into postfix notation using
        shunting_yard_service
        - evaluating the postfix notation

        Args:
            expression (Expression): Expression object

        Returns:
            float: value of the expression
        """
        self._validation_service.validate_expression(expression)
        expression = self._parser_service.parse_to_tokens(
            expression=expression,
            variables=self.variables()
        )
        expression = self._shunting_yard_service.run(expression)
        result = self._evaluate_postfix_notation(expression.postfix())
        return result

    def _calculate_basic_operation(
            self,
            token: str,
            stack: list
    ) -> str:
        operand_1 = stack.pop()
        operand_2 = stack.pop()
        if token == "^":
            token = "**"
        # TODO: do this using ast; https://stackoverflow.com/questions/2371436/evaluating-a-mathematical-expression-in-a-string
        return str(eval(operand_2 + token + operand_1))

    def _calculate_one_parameter_function(
            self,
            token: str,
            stack: list
    ) -> str:
        """
        Calculates value of one parameter functions.
        e.g. sin(90)

        Args:
            token (str): token
            stack (list): stack 

        Returns:
            str: value of function as string
        """
        operand = stack.pop()
        value = SUPPORTED_FUNCTIONS[token](float(operand))
        return str(value)

    def _calculate_two_parameter_function(
            self,
            token: str,
            stack: list
    ) -> str:
        """
        Calculates value of function with two parameters.
        e.g. max(2,3)

        Args:
            token (str): token
            stack (list): stack

        Returns:
            str: value of function as string
        """
        operand_2 = stack.pop()
        operand_1 = stack.pop()
        result = SUPPORTED_FUNCTIONS[token](float(operand_1), float(operand_2))
        return str(result)

    def _evaluate_postfix_notation(
            self,
            postfix_notation: list
    ) -> float:
        """
        Calculate the value of the expression from postfix notation

        Args:
            postfix_notation (list): postfix notation

        Returns:
            float: calculated value
        """
        stack = []
        for token in postfix_notation:
            if self._validation_service.is_number(token):
                stack.append(token)
            elif self._validation_service.is_one_parameter_function(token):
                stack.append(
                    self._calculate_one_parameter_function(token, stack)
                )
            elif self._validation_service.is_two_parameter_function(token):
                stack.append(
                    self._calculate_two_parameter_function(token, stack)
                )
            else:
                stack.append(
                    self._calculate_basic_operation(token, stack)
                )

        value = float(stack.pop())
        return value


calculator_service = CalculatorService()

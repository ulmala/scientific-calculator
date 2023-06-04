from ast import literal_eval
from entities.expression import Expression
from services.shunting_yard_service import (
    shunting_yard_service as default_shunting_yard_service
)


class CalculatorService:
    """
    Responsible for executing the high level calculation logic
    """
    def __init__(
            self,
            shunting_yard_service=default_shunting_yard_service
    ) -> None:
        """
        Class constructor

        Args:
            shunting_yard_service (ShuntingYardService): Defaults to default_shunting_yard_service.
        """
        self._shunting_yard_service = shunting_yard_service

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
        expression = self._shunting_yard_service.run(expression)
        result = self._evaluate_postfix_notation(expression.postfix())
        return result

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
            if token.isdigit():
                stack.append(token)
            else:
                val_1 = stack.pop()
                val_2 = stack.pop()
                stack.append(str(eval(val_2 + token + val_1))) # TODO: do this using ast; https://stackoverflow.com/questions/2371436/evaluating-a-mathematical-expression-in-a-string

        result = float(stack.pop())
        return result


calculator_service = CalculatorService()

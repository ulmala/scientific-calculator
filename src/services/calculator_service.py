from entities.expression import Expression
from services.shunting_yard_service import (
    shunting_yard_service as default_shunting_yard_service
)


class CalculatorService:
    def __init__(
            self,
            shunting_yard_service=default_shunting_yard_service
    ) -> None:
        self._shunting_yard_service = shunting_yard_service

    def solve(
            self,
            expression: Expression
    ):
        expression = self._shunting_yard_service.run(expression)
        result = self._evaluate_postfix_notation(expression.postfix())
        return result

    def _evaluate_postfix_notation(
            self,
            postfix_notation: list
    ) -> int:
        stack = []
        for token in postfix_notation:
            if token.isdigit():
                stack.append(token)
            else:
                val_1 = stack.pop()
                val_2 = stack.pop()            
                stack.append(str(eval(val_2 + token + val_1)))

        result = float(stack.pop())
        return result

calculator_service = CalculatorService()

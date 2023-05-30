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
        self._shunting_yard_service.run(expression)

calculator_service = CalculatorService()

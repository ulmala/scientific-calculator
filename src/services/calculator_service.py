from entities.equation import Equation
from algorithms.shunting_yard2 import (
    shunting_yard as default_shunting_yard
)


class CalculatorService:
    def __init__(
            self,
            shunting_yard=default_shunting_yard
    ) -> None:
        self._shunting_yard = shunting_yard

    def solve(
            self,
            equation: Equation
    ):
        self._shunting_yard.run(equation)

calculator_service = CalculatorService()

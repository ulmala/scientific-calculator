from services.calculator_service import calculator_service, NotValidVariable
from services.validation_service import validation_service
from services.validation_service import NotValidExpression


class UI:
    def __init__(
            self,
            calculator_service=calculator_service
    ) -> None:
        self._calculator_service = calculator_service

    def _handle_add_variable(
            self,
            var_name=None,
            var_value=None
    ):
        if not var_name and not var_value:
            var_name = input("Variable name: ")
            var_value = input("Variable value: ")
        try:
            self._calculator_service.add_variable(
                variable_name=var_name,
                variable_value=str(var_value)
            )
        except NotValidVariable as e:
            print(f"*!*!*!*!*!*! {e} *!*!*!*!*!*!")

    def start(self):
        while True:
            for _ in range(100): print("#", end="")
            print()
            user_input = input(
                "Type 'var' to declare new variable or 'exp' to submit expression: "
            )

            if user_input == "exp":
                user_expression = input("Type your equation here: ")
                try:
                    expression = calculator_service.solve(user_expression)
                except NotValidExpression as e:
                    print(f"*!*!*!*!*!*! {e} *!*!*!*!*!*!")
                    continue

                print(expression)

                user_input = input(
                    "Enter variable name to store the result into variable (else press Enter): "
                )
                if user_input != "":
                    self._handle_add_variable(
                        var_name=user_input,
                        var_value=expression.value
                    )

            if user_input == "var":
                self._handle_add_variable()

            print(calculator_service.list_variables())

from services.calculator_service import calculator_service
from services.validation_service import validation_service
from services.validation_service import NotValidExpression


class UI:
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

                #print(expression)

                user_input = input(
                    "Enter variable name to store the result into variable (else press Enter): "
                )
                if user_input == "":
                    continue
                calculator_service.add_variable(
                    variable_name=user_input,
                    variable_value=str(expression.value)
                )

            if user_input == "var":
                var_name = input("Variable name: ")
                if not validation_service.is_valid_variable_name(var_name):
                    print(f"{var_name} is not a valid variable name!")
                    continue
                var_value = input("Variable value: ")
                if not validation_service.is_number(var_value):
                    print(f"{var_value} is not a valid variable value!")
                    continue
                calculator_service.add_variable(
                    variable_name=var_name, variable_value=var_value)
            print(calculator_service.list_variables())

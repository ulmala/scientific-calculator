from services.calculator_service import calculator_service
from services.parser_service import parser_service
from services.validation_service import validation_service
from services.validation_service import NotValidExpression
from entities.expression import Expression


class UI:
    def start(self):
        while True:
            for _ in range(2):
                print("\n")
            user_input = input(
                "Type 'var' to declare new variable or 'exp' to submit expression: ")
            if user_input == "exp":
                user_expression = input("Type your equation here: ")
                expression = Expression(user_expression)
                try:
                    result = calculator_service.solve(expression)
                except NotValidExpression as e:
                    print(f"*!*!*!*!*!*! {e} *!*!*!*!*!*!")
                    continue

                print(f"{' '.join(expression.tokens)} =", result)

                user_input = input(
                    "Do you want to save the result to variable? Press enter to continue, else write variable name: "
                )
                if user_input == "":
                    continue
                calculator_service.add_variable(
                    variable_name=user_input,
                    variable_value=str(result)
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
                calculator_service.print_variables()

            input("\nPress any key to continue")

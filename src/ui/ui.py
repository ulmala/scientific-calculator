from services.calculator_service import calculator_service
from services.parser_service import parser_service
from entities.equation import Equation

class UI:
    def start(self):
        user_input = input("submit equation: ")
        if user_input == "q":
            return
        else:
            equation = Equation(user_input)

        if parser_service.validate_equation(equation):
            parser_service.parse_to_tokens(equation)
            print(equation.tokens())
        else:
            print("not a valid equation!")

        calculator_service.solve(equation)
        
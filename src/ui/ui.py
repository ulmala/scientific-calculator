from services.calculator_service import calculator_service
from services.parser_service import parser_service
from entities.expression import Expression

class UI:
    def start(self):
        user_input = input("submit expression: ")
        if user_input == "q":
            return
        else:
            expression = Expression(user_input)

        if parser_service.validate_expression(expression):
            parser_service.parse_to_tokens(expression)
            print(expression.tokens())
        else:
            print("not a valid expression!")

        result = calculator_service.solve(expression)
        print(result)
        
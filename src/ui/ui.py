import sys
from services.calculator_service import calculator_service, NotValidVariable
from services.validation_service import NotValidExpression

from config import OPERATORS, SUPPORTED_FUNCTIONS


class UI:
    def __init__(
            self,
            calculator_service=calculator_service,
            line_length=80,
            header="Scientific Calculator"
    ) -> None:
        self._calculator_service = calculator_service
        self._line_length = line_length
        self._header = header

    def _handle_add_variable(
            self,
            var_name=None,
            var_value=None
    ) -> None:
        """
        Implements adding new user defined variable into the calculator.

        Args:
            var_name (str, optional): variable name. Defaults to None.
            var_value (str, optional): variable value. Defaults to None.
        """
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

    def _show_instructions(self) -> None:
        """
        Prints calculator instructions
        """
        print("\n\033[4mOPERATORS\033[0m:")
        print("This calculator supports following  arithmetic operators:")
        print(",   ".join(OPERATORS), "\t\t(NOTE: '^' is power operator)")

        print("\n\033[4mFUNCTIONS\033[0m:")
        print("\nAnd this calculator supports following functions: ")
        print("   ".join(SUPPORTED_FUNCTIONS))
        
        print("\n\033[4mVARIABLES\033[0m:")
        print("You can define custom variables which can be used in expressions.")
        print("Variable must be single alphabet and the assigned value must be number")

        print("\n\nYou can view theses instructions any time by typing 'help'")
        print("Press any key to continue")
        input()

    def _show_header(self) -> None:
        """
        Prints application header
        """
        pad_len = (self._line_length - len(self._header)) // 2
        print("".join(["="] * self._line_length))
        print(
            " " * pad_len + self._header + " " *
             (pad_len + (self._line_length - len(self._header)) % 2)
        )
        print("".join(["="] * self._line_length))
        
    def _show_variables(self) -> None:
        """
        Prints declared variables (if any)
        """
        if len(calculator_service.list_variables()) == 0:
            print("No variables declared yet")
        else:
            print(calculator_service.list_variables())

    def start(self):
        self._show_header()
        self._show_instructions()
        while True:
            print("\n\n\n")
            print("".join(["="] * self._line_length))
            print()
            print(
                "Type:\n"
                "- 'var' to declare new varibale\n"
                "- 'vars' to list declared variables\n"
                "- 'exp' to submit expression\n"
                "- 'help' for instructions\n"
            )
            user_input = input(">>")

            if user_input == "help":
                self._show_instructions()
                continue

            if user_input == "exp":
                user_expression = input("Type your equation here: ")
                try:
                    expression = calculator_service.solve(user_expression)
                except NotValidExpression as e:
                    print(f"*!*!*!*!*!*! {e} *!*!*!*!*!*!")
                    continue

                print(f"\n\033[4mResult:{expression}\033[0m")


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

            if user_input == "vars":
                self._show_variables()

            input("\nPress any key to continue")
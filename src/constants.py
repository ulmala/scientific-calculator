import math


OPERATOR_PRECEDENCE = {
    "(": 0,
    "-": 1,
    "+": 1,
    "/": 2,
    "*": 2,
    "^": 3
}

OPERATORS = ["+", "-", "*", "/", "^"]
LEFT_ASSOCIATIVE_OPERATORS = ["+", "-", "*", "/"]

SUPPORTED_FUNCTIONS = {
    "sin": math.sin,
    "max": max
}

ONE_PARAMETER_FUNCTIONS = ["sin"]
TWO_PARAMETER_FUNCTIONS = ["max"]

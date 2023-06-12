# Implementation document

## Structure

Current source code is structured as follows:

```
src
├── calculator.py
├── config.py
├── entities
│   ├── expression.py
│   ├── operator_stack.py
│   └── output_queue.py
├── services
│   ├── calculator_service.py
│   ├── parser_service.py
│   ├── shunting_yard_service.py
│   └── validation_service.py
├── tests
│   ├── entities
│   └── services
└── ui
    └── ui.py
```

### Description of each file
`calculator.py`:  
Launches the application.

`config.py`:  
Contains general configurations for the calculator, such as which functions are supported in the calculator.

`entities/expression.py`:  
Class to represent the expression and its different forms, such as postfix notation.

`entities/operator_stack.py`:  
Class to represent the operator stack which is used in the Shunting Yard algorithm.  

`entities/output_queue.py`:  
Class to represent the output queue which is used in the Shunting Yard algorithm.  

`services/calculator_service.py`:  
Responsible for executing the high level logic of the calculation process. Also responsible for executing the mathematical operations.  

`services/parser_service.py`:  
Responsible for parsing the user's expressions.  

`services/shunting_yard_service.py`:  
The actual Shunting yard algorithm.  

`services/validation_service.py`:  
Responsible for offering different kind of validation methods.  

`tests/*.py`:  
All tests.  

`ui/ui.py`:  
Application's command line user interface.


## References
1. https://en.wikipedia.org/wiki/Shunting_yard_algorithm
# Specification document

## General

Programme: Bachelor's Programme in Computer Science  
Project language: English  
Project programming language: Python  

Outcome of this project is a scientific calculator which has a command line user interface. User can submit equations into the program and the calculator will solve them (and they need to be solved correctly).


## Algorithms and data structures used
Calculator will use Shunting yard algorithm [1] for parsing the user's input. Algorithm itself is stack-based so stack data structure [2] is used. Also user's input equation will firslty be parsed into list data structure [3].

## Inputs
User's can submit equations into the calculator using command line user interface. Inputs can contain numbers, mathematical operators, functions (few functions will be supported, TBD which ones when the project proceeds) and variables (at least one variable equations will be supported, TBD if multivariable support when the project proceeds).  

Example:  
``>> Type "var" to declare new variable or "eq" to submit equation: var``  
``>> Name of the variable: x``  
``>> Value of the variable: 10``  
``>> Type "var" to declare new variable or "eq" to submit equation: eq`` 
``>> Equation: 2 * x + 1``  
``>> Result: 21``  

If the submitted equation is not valid, e.g. havig mismatched parentheses or equation starting with operator, the program will prompt error message for the user (TBD how detailed messages are prompted).  

Example:  
``>> ...``  
``>> Equation: (2 * x + 1``  
``>> Invalid equation, check typing!``    

## Time and space complexity
Algorithm's target time complexity is $O(n)$ and it's target space complexity is also $O(n)$.

## References
1. https://en.wikipedia.org/wiki/Shunting_yard_algorithm
2. https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
3. https://en.wikipedia.org/wiki/List_(abstract_data_type)
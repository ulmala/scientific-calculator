# Test document

Current test coverage:  
| Name                                    |    Stmts |     Miss |   Branch |   BrPart |   Cover |
|---------------------------------------- | -------: | -------: | -------: | -------: | ------: |
| src/constants.py                        |        3 |        0 |        0 |        0 |    100% |
| src/entities/expression.py              |       23 |        0 |        0 |        0 |    100% |
| src/entities/operator\_stack.py         |       22 |        0 |        4 |        0 |    100% |
| src/entities/output\_queue.py           |       12 |        0 |        0 |        0 |    100% |
| src/services/calculator\_service.py     |       21 |       21 |        4 |        0 |      0% |
| src/services/parser\_service.py         |       29 |        0 |       12 |        0 |    100% |
| src/services/shunting\_yard\_service.py |       57 |       30 |       26 |        0 |     37% |
|                               **TOTAL** |  **167** |   **51** |   **46** |    **0** | **64%** |
  
More detailed report can be created running `poetry run invoke coverage-report`.  
# Test document

Current test coverage:  
| Name                                    |    Stmts |     Miss |   Branch |   BrPart |   Cover |
|---------------------------------------- | -------: | -------: | -------: | -------: | ------: |
| src/config.py                           |        7 |        0 |        0 |        0 |    100% |
| src/entities/expression.py              |       23 |        0 |        0 |        0 |    100% |
| src/entities/operator\_stack.py         |       29 |        0 |        8 |        0 |    100% |
| src/entities/output\_queue.py           |       12 |        0 |        0 |        0 |    100% |
| src/services/calculator\_service.py     |       53 |       10 |       12 |        0 |     82% |
| src/services/parser\_service.py         |       21 |        0 |        6 |        0 |    100% |
| src/services/shunting\_yard\_service.py |       55 |        3 |       26 |        2 |     94% |
| src/services/validation\_service.py     |       71 |        4 |       25 |        4 |     92% |
|                               **TOTAL** |  **271** |   **17** |   **77** |    **6** | **93%** |
  
More detailed report can be created running `poetry run invoke coverage-report`.  
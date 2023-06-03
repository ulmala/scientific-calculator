# scientific-calculator
University of Helsinki course: Data structures and Algorithms Lab  

## Weekly reports
- [week 1](documentation/weekly_reports/week_1.md)
- [week 2](documentation/weekly_reports/week_2.md)
- [week 3](documentation/weekly_reports/week_3.md)

## Setup guide

1. Install required dependencies

```bash
poetry install
```

2. Start the program

```bash
poetry run invoke start
```

## Command line commands

Start the program: 
```bash
poetry run invoke start
```
Run tests:  

```bash
poetry run invoke test
```
Create test coverage report:

```bash
poetry run invoke coverage-report
```
Run code style checking with pylint:
```bash
poetry run invoke lint
```
# scientific-calculator
University of Helsinki course: Data structures and Algorithms Lab  

## Weekly reports
- [week 1](documentation/weekly_reports/week_1.md)
- [week 2](documentation/weekly_reports/week_2.md)
- [week 3](documentation/weekly_reports/week_3.md)
- [week 4](documentation/weekly_reports/week_4.md)

## Setup guide

1. This project uses Poetry, install it before use. Installation guide [here](https://python-poetry.org/docs/#installation)

2. Clone this repo or download the code, then `cd scientific-calculator``

3. Install required dependencies:

```bash
poetry install
```

4. And start the program

```bash
poetry run invoke start
```

## Other command line commands
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
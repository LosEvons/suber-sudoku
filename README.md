# suber-sudoku
A sudoku game programmed in Python as an exercise on writing good, maintainable and understandable code.

## Setup instructions
1. **Make sure you have poetry installed**
    You may install poetry from the official website: [Poetry Installation](https://python-poetry.org/docs/)

2. **Clone this repository**
3. **Install dependencies with poetry**
```poetry install```
4. **Run the app**
```poetry run invoke run```

#### Other useful commands
- Run unittests with ```poetry run invoke unittest```
- Generate a HTML test coverage report with ```poetry run invoke coverage_report```
- Run lint with ```poetry run invoke lint```
- Run typecheck with ```poetry run invoke typecheck```
- Run all of of the above with ```poetry run invoke report```

Configurations for lint and type checking can be found in the root dirtectory files mypy.ini and .pylintrc. Dependencies are listed in pyproject.toml.

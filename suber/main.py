"""suber/main.py"""
from ui.app import SudokuApp

def main() -> None:
    """The main function and entry point of the program."""
    app = SudokuApp()
    app.run()

if __name__ == '__main__':
    main()

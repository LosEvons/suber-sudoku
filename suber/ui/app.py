"""suber/ui/app.py"""

from utils.constants import ROOT_DIR
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Button, Static

class SudokuApp(App):
    """A textual app to play Sudoku."""

    CSS_PATH = ROOT_DIR + "/static/styles.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit")
        ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield SudokuGrid()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    async def action_quit(self) -> None:
        self.exit()

class SudokuCell(Static):
    """A widget to display a single sudoku grid cell."""

    def compose(self) -> ComposeResult:
        yield Button("Cell", classes="sudoku-cell", variant="success")

class SudokuGrid(Static):
    """A widget to display a sudoku grid"""
    def compose(self) -> ComposeResult:
        yield Container(SudokuCell(), SudokuCell(), SudokuCell())
        yield Container(SudokuCell(), SudokuCell(), SudokuCell())
        yield Container(SudokuCell(), SudokuCell(), SudokuCell())

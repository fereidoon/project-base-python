import random

# Module-level constants
WIN_COMBINATIONS = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7),
]
EMPTY = ' '


class TicTacToe:
    def __init__(self) -> None:
        # index 0 unused; board positions 1..9
        self.board = [EMPTY] * 10
        self.current_player = None
        self.winner = None

    # --- player selection / turn handling ---
    def choose_starting_player(self) -> str:
        """Pick a starting player ('x' or 'o') and set current_player."""
        self.current_player = random.choice(['x', 'o'])
        return self.current_player

    # backward-compatible alias for old name
    def choose_player(self) -> str:
        return self.choose_starting_player()

    def switch_turn(self) -> str:
        """Toggle current_player and return the new current player."""
        if self.current_player == 'x':
            self.current_player = 'o'
        else:
            self.current_player = 'x'
        return self.current_player

    # backward-compatible alias for old name
    def change_turn(self) -> str:
        return self.switch_turn()

    # --- move handling (separate I/O from logic) ---
    def get_move_from_user(self) -> int | None:
        """Read and validate a move from input. Return 1-9 or None on invalid."""
        try:
            choice = int(input("Enter your choice (1-9): ").strip())
        except ValueError:
            print("Please enter a number between 1 and 9.")
            return None

        if not 1 <= choice <= 9:
            print("Choice must be between 1 and 9.")
            return None

        if self.board[choice] != EMPTY:
            print('Cell already taken. Choose another.')
            return None

        return choice

    def apply_move(self, move_index: int) -> bool:
        """Apply a validated move index (1-9). Return True if applied."""
        if not (1 <= move_index <= 9):
            return False
        if self.current_player is None:
            # no player selected
            return False
        if self.board[move_index] != EMPTY:
            return False
        self.board[move_index] = self.current_player
        return True

    
    def make_move(self) -> bool:
        choice = self.get_move_from_user()
        if choice is None:
            return False
        return self.apply_move(choice)

    # --- display ---
    def show_board(self, show_indices: bool = True) -> None:
        """Print the board as a 3x3 grid.

        If show_indices is True, empty cells are shown as their position number
        (1-9) to help the player choose a move. Otherwise empty cells are blank.
        """
        def _cell_text(i: int) -> str:
            if self.board[i] != EMPTY:
                return self.board[i]
            return str(i) if show_indices else ' '

        for start in (1, 4, 7):
            a = _cell_text(start)
            b = _cell_text(start + 1)
            c = _cell_text(start + 2)
            print(f" {a} | {b} | {c} ")
            if start < 7:
                print("---+---+---")

    # --- game status ---
    def check_winner(self):
        """Return 'x' or 'o' if there's a winner, 'Draw' if board full, otherwise None."""
        for a, b, c in WIN_COMBINATIONS:
            if self.board[a] == self.board[b] == self.board[c] != EMPTY:
                self.winner = self.board[a]
                return self.winner

        # Check for draw (no empty spaces in positions 1..9)
        if EMPTY not in self.board[1:]:
            self.winner = 'Draw'
            return 'Draw'

        return None

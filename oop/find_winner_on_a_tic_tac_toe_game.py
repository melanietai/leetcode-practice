"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.
"""

class Solution:

    def tictactoe(self, moves: List[List[int]]) -> str:
        size = 3
        self.board(size)
        player = self.player()

        while moves:
            row, col = moves[0]
            moves = moves[1:]
            self.move(row, col, player)

            if self.is_winner(size, row, col, player):
                if player == "X":
                    return "A"
                else:
                    return "B"
            if self.is_board_filled(size):
                if moves:
                    return "Pending"
                else:
                    return "Draw"
            player = self.player(player)
        return "Pending"
    
    
    def player(self, player = None):
        if not player or player == "O":
            return "X"
        else:
            return "O"
        
    def board(self, size):
        self.board = []
        for i in range(size):
            self.board.append([" "] * 3)
        return self.board
    
    def move(self, row, col, player):
        self.board[row][col] = player
    
    def check_horizontal(self, size, row, player):
        for j in range(size):
            if self.board[row][j] != player:
                return False
        return True
    
    def check_vertical(self, size, col, player):
        for i in range(size):
            if self.board[i][col] != player:
                    return False
        return True
    
    def check_diagonal(self, size, player):
        for i in range(size):
            if self.board[i][i] != player:
                return False
        return True
    
    def check_rev_diagonal(self, size, player):
        for i in range(size):
            if self.board[i][size-i-1] != player:
                return False
        return True
    
    def is_winner(self, size, row, col, player):
        if self.check_vertical(size, col, player) or self.check_horizontal(size, row, player) or self.check_diagonal(size, player) or self.check_rev_diagonal(size, player):
            return True
    
    def is_board_filled(self, size):
        for i in range(size):
            for j in range(size):
                if self.board[i][j] == " ":
                    return False
        return True
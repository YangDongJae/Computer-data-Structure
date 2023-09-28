import random

#class data type if coulnd't use class notion, it is not data type. 
import random

class Matrix:
    def __init__(self, rows, cols, f):
        self.M = []
        if f == 'r':
            self.rMatrix(rows, cols)
        elif f == 'z':
            self.zMatrix(rows, cols)

    def rMatrix(self, rows, cols):
        for _ in range(rows):
            self.M.append([random.randint(1, 10) for _ in range(cols)])

    def zMatrix(self, rows, cols):
        for _ in range(rows):
            self.M.append([0] * cols)

    def mPrint(self):
        for row in self.M:
            print(row)

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.M])

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if len(self.M) != len(other.M) or len(self.M[0]) != len(other.M[0]):
            raise ValueError("Matrix dimensions do not match for addition")
        
        result = Matrix(len(self.M), len(self.M[0]), 'z')
        for i in range(len(self.M)):
            for j in range(len(self.M[0])):
                result.M[i][j] = self.M[i][j] + other.M[i][j]
        
        return result

    def __sub__(self, other):
        if len(self.M) != len(other.M) or len(self.M[0]) != len(other.M[0]):
            raise ValueError("Matrix dimensions do not match for subtraction")
        
        result = Matrix(len(self.M), len(self.M[0]), 'z')
        for i in range(len(self.M)):
            for j in range(len(self.M[0])):
                result.M[i][j] = other.M[i][j] - self.M[i][j]  # Subtract Matrix A from Matrix B
        
        return result

    def __mul__(self, other):
        if len(self.M[0]) != len(other.M):
            raise ValueError("Matrix dimensions are not compatible for multiplication")
        
        result = Matrix(len(self.M), len(other.M[0]), 'z')
        for i in range(len(self.M)):
            for j in range(len(other.M[0])):
                result.M[i][j] = sum(self.M[i][k] * other.M[k][j] for k in range(len(self.M[0])))
        
        return result


    def transpose(self):
        rows, cols = len(self.M), len(self.M[0])
        result = Matrix(cols, rows, 'z')
        for i in range(rows):
            for j in range(cols):
                result.M[j][i] = self.M[i][j]
        
        return result
    
import random

class EightQueens:
    rnb = random.Random()
    
    def __init__(self):
        self.board = list(range(8))
    
    def runEQ(self, nos):
        found = 0
        tries = 0
        
        while found < nos:
            EightQueens.rnb.shuffle(self.board)
            tries += 1
            if not self.has_clash():
                found += 1
                print("Solution: {}, {}".format(found, self.board))
                tries = 0
    
    def has_clash(self):
        for col in range(1, len(self.board)):
            if self.col_clashes(col):
                return True
        return False
    
    def col_clashes(self, col):
        for i in range(col):
            if self.dclashes(i, self.board[i], col, self.board[col]):
                return True
        return False
    
    def dclashes(self, x0, y0, x1, y1):
        d1 = abs(x0 - x1)
        d2 = abs(y0 - y1)
        return d1 == d2

class TicTacToe:
    def __init__(self):
        self.board = [-1] * 9  # Using a 1D list to represent the 3x3 board
        self.current_player = 0  # Player 0 (X) goes first

    def play_ttt(self):
        win = False
        move = 0

        while not win and move < 9:  # The game ends after 9 moves
            self.print_board()

            if self.current_player == 0:
                turn = 'X'
            else:
                turn = 'O'

            print(f"Turn for player {turn}")
            user = self.get_input()

            while self.board[user] != -1:
                print("Invalid Input. Try again.")
                user = self.get_input()

            self.board[user] = self.current_player
            move += 1

            if move > 4:  # A player needs at least 5 moves to win
                winner = self.check_win()
                if winner != -1:
                    self.print_board()
                    print(f"The winner is {'X' if winner == 0 else 'O'}!")
                    return

            self.current_player = 1 - self.current_player  # Switch player

        self.print_board()
        print("It's a draw!")

    def get_input(self):
        while True:
            try:
                user = int(input("Enter a position (0-8): "))
                if 0 <= user <= 8:
                    return user
                else:
                    print("Invalid input. Enter a number between 0 and 8.")
            except ValueError:
                print("Invalid input. Enter a number between 0 and 8.")

    def check_win(self):
        win_cords = ((0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                     (0, 4, 8), (2, 4, 6))            # Diagonals

        for cord in win_cords:
            a, b, c = cord
            if self.board[a] == self.board[b] == self.board[c] != -1:
                return self.board[a]

        return -1

    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.display_symbol(self.board[i])} | {self.display_symbol(self.board[i + 1])} | {self.display_symbol(self.board[i + 2])}")
            if i < 6:
                print("-" * 9)

    @staticmethod
    def display_symbol(player):
        if player == 0:
            return 'X'
        elif player == 1:
            return 'O'
        else:
            return ' '
# Task 6: More on Classes

# Task 6: step 2
# declare class TictactoeException that  inherit from the Exception class. 
class TictactoeException(Exception):

    # Add an __init__ method 
    def __init__(self, message):
                 
        #stores an instance variable called message
        self.message = message

        #calls the __init__ method of the superclass
        super().__init__(message)

# Task 6: step 3
# Declare also a class called Board. 
class Board:

    # The Board class that has  variable called valid_moves
    valid_moves=["upper left", "upper center", "upper right",
                  "middle left", "center", "middle right", 
                  "lower left", "lower center", "lower right"]
    
    # __init__ function that only has the self argument
    def __init__(self):

         # Create a 3x3 list of lists, all containing a space " "
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]

        # Create instance variables self.turn, which is initialized to "X"
        self.turn = "X"

    # Task 6: step 1(part 2)

    # Add a __str__() method- converts the board into a displayable string
    def __str__(self):
        
        # show the current state of the game
        lines = []

        #  The rows to be displayed are separated by newlines ("\n") 
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    
    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3 # row
        column = move_index % 3 #column
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
    
    def whats_next(self):
        # check for cat's Game 
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                else:
                    continue
                break
            else:
                continue
            break
        if (cat):
            return (True, "Cat's Game.")
        
        # Check for win
        win = False
        for i in range(3): # check rows
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        if not win:
            for i in range(3): # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != " ": # check diagonals
                if self.board_array[0][0] ==  self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] ==  self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True

        # Determine return state            
        if  win:
            # if win is true then winner is the player who just moved
            winner = "0" if self.turn == "X" else "x"
            return (True, f"{winner} wins")
        if cat:
            return(True, "CAt's Game.")
        return(False, f"{self.turn}'s turn.")
    
# Mainline Game loop
if __name__ == "__main__":
    game_board = Board()
    over = False

    print("TicTacToe Started")
    print(game_board)

    while not over:
        prompt = f"{game_board.turn}'s turn. Enyter move: "
        user_input = input(prompt).strip().lower()

        try:
            game_board.move(user_input)
            print(game_board)
            over, message = game_board.whats_next()
            print(message)
        except TictactoeException as e:
            print(f"------Error: {e.message} ----")


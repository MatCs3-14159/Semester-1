board = [ ['1','2','3'],\
              ['4','5','6'],\
              ['7','8','9']]

def draw_board(board):
    print("                 ", end = " ")
    print(" --------------  ")
    for row in range(3):
        print("                 ", end = " ")
        print(' |  ' + board[row][0] + '  |  ' + board[row][1] + '  |  ' + board[row][2] + '  | ')
        print("                 ", end = " ")
        print(" --------------  ")

def welcome(board):
    """
    Prints the welcome message and displays the board layout.
    """
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print('The board layout is shown below:')
    draw_board(board)
    print('When prompted, enter the number corresponding to the square you want.')



def initialise_board(board):
    """
    Sets all elements of the board to a single space ' '.
    """
    return [[' ' for col in range(3)] for row in range(3)]

def move(board):
    while True:
        try:
            print("                         1 2 3  ")
            print("                         4 5 6  ")
            choice = int(input("Choose your square: 7 8 9 : "))
            if choice < 1 or choice > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            row = (choice - 1) // 3
            col = (choice - 1) % 3
            if board[row][col] == ' ':
                 return row, col 
            else:
                print("That square is already taken. Please choose another square.")
        except ValueError:
            print("Please enter a valid integer.")





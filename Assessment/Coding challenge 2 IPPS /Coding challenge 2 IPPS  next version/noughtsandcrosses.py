import random
import os.path
import json


random.seed()


DIFFICULTY = "easy"

def draw_board(board):
    """
    Draws the noughts and crosses board.
     -----------------   
    |  1  |  2  |  3  | 
     -----------------   
    |  4  |  5  |  6  | 
     -----------------   
    |  7  |  8  |  9  | 
     -----------------   
    """
    print()
    print(" "*17 + "   --------------   ")
    for row in board:
        print(" "*17 + '  |  ' + '  |  '.join(row) + '  | ')
        print(" "*17 + "   --------------   ")
    print()

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

def get_player_move(board):
    """
    Ask the user for the cell to put the X in.

    Return: row, col 
    """
    while True:
        try:
            print("                         1 2 3  ")
            print("                         4 5 6  ")
            move = int(input("Choose your square: 7 8 9 : "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] == ' ':
                return row, col
            else:
                print("That square is already taken. Please choose another square.")
        except ValueError:
            print("Please enter a valid integer.")
        except Exception as e:
            print(f"An error occurred: {e}")


def computer_move_easy(board):
    available_moves = [(r,c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    if available_moves:
        return random.choice(available_moves)
    return None, None


def computer_move_medium(board):
    # 1. Try to win
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = 'O'
                if check_for_win(board, 'O'):
                    board[r][c] = ' '
                    return r, c
                board[r][c] = ' '

    # 2. Block player win
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = 'X'
                if check_for_win(board, 'X'):
                    board[r][c] = ' '
                    return r, c
                board[r][c] = ' '

    # 3. Otherwise random
    return computer_move_easy(board)


def minimax(board, is_maximizing):
    if check_for_win(board, 'O'):
        return 1
    if check_for_win(board, 'X'):
        return -1
    if check_for_draw(board):
        return 0

    if is_maximizing:
        best_score = -999
        for r in range(3):
            for c in range(3):
                if board[r][c] == ' ':
                    board[r][c] = 'O'
                    score = minimax(board, False)
                    board[r][c] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = 999
        for r in range(3):
            for c in range(3):
                if board[r][c] == ' ':
                    board[r][c] = 'X'
                    score = minimax(board, True)
                    board[r][c] = ' '
                    best_score = min(best_score, score)
        return best_score


def computer_move_hard(board):
    best_score = -999
    best_move = None

    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = 'O'
                score = minimax(board, False)
                board[r][c] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (r, c)

    return best_move


def choose_computer_move(board):
    print(f"Computer is choosing a move... ({DIFFICULTY.upper()})")

    if DIFFICULTY == "easy":
        return computer_move_easy(board)

    elif DIFFICULTY == "medium":
        return computer_move_medium(board)

    else:  # hard
        return computer_move_hard(board)


def check_for_win(board, mark):

    for row in board:
        if all(cell == mark for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False


def check_for_draw(board):

    return all(cell != ' ' for row in board for cell in row)


def play_game(board):
    """
    Runs the main game loop where player and computer plays turn by turn.

    Parameter: 
        board (list): A 3x3 list that represents the game board.

    Return: 
        int: 1 if the player wins, -1 if the computer wins, 0 if it's a draw.
    """

    board = initialise_board(board)
    draw_board(board)

    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)

        if check_for_win(board, 'X'):
            print(" 🥇 Congratulations! You won! 🥇 ")
            return 1
        
        if check_for_draw(board):
            print(" 🤝 It's a draw! 🤝 ")
            return 0
        
        #Computers Turn 
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        
        if check_for_win(board, 'O'):
            print(" 🤖 Computer won! Better Luck Next Time! 🤖 ")
            return -1
        if check_for_draw(board):
            print(" 🤝 It's a draw! 🤝 ")
            return 0
                    
                
def menu():
    global DIFFICULTY
    print("\nChoose an option:")
    print("1 - Play the game")
    print("2 - Save score")
    print("3 - Load and display the scores")
    print("q - Quit")

    choice = input("Your choice: ").lower()

    if choice == "1":
        while True:
            print("\nChoose difficulty:")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard (Unbeatable)")
            d = input("Your choice: ")

            if d == "1":
                DIFFICULTY = "easy"
                break
            elif d == "2":
                DIFFICULTY = "medium"
                break
            elif d == "3":
                DIFFICULTY = "hard"
                break
            else:
                print("Invalid difficulty. Try again.")

    return choice


def load_scores():

    if not os.path.exists('leaderboard.txt'):
        return {}
    with open('leaderboard.txt', 'r') as file:
        return json.load(file)


def save_score(score):

    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = leaders.get(name, 0) + 1
    with open('leaderboard.txt', 'w') as file:
        json.dump(leaders, file)


def display_leaderboard(leaders):
    
    print("\nLeaderboard:")
    for name, score in sorted(leaders.items(), key=lambda item: item[1], reverse=True):
        print(f"{name}: {score}")

"""
    Noughts and Crosses (Tic-Tac-Toe) Game
    --------------------------------------

    This Python program allows a user to play the classic game of Noughts and Crosses (Tic-Tac-Toe) 
    against the computer. The game is menu-driven and includes features such as:

    Features:
    - Display of a 3x3 game board with numbered squares for easy selection.
    - Safe user input handling: only allows valid, empty squares to be chosen.
    - Computer opponent that chooses moves randomly.
    - Win and draw detection for both player and computer.
    - Saving and loading of scores using a file-based leaderboard (JSON format).
    - Simple menu system to play the game, save scores, view leaderboard, or quit.

    Modules / Functions:
    - draw_board(board): Display the current game board.
    - welcome(board): Prints a welcome message and shows the initial board.
    - initialise_board(board): Initializes the board with empty spaces.
    - get_player_move(board): Gets a valid move from the player.
    - choose_computer_move(board): Chooses a random valid move for the computer.
    - check_for_win(board, mark): Checks if the given mark has won.
    - check_for_draw(board): Checks if the board is full without a winner.
    - play_game(board): Runs the main game loop.
    - menu(): Displays the menu and takes user choice.
    - save_score(score): Saves the player’s score to the leaderboard file.
    - load_scores(): Loads and returns the leaderboard data.
    - display_leaderboard(leaders): Prints the leaderboard in descending order.

    Usage:
    - Run the script and follow the menu prompts to play the game.
    - Enter a number 1-9 to place your mark on the board.
    - Use the menu to save or view scores.

    Author: Sagar Mishra
    Student ID: 2606063
    Date: 2 feb 2026
"""


import random
import os.path
import json


random.seed()


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

    Parameter: 
        board (list): A 3x3 list that represents the game board.
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

    Parameter: 
        board (list): A 3x3 list that represents the game board.

    Return: no return
    """
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print('The board layout is shown below:')
    draw_board(board)
    print('When prompted, enter the number corresponding to the square you want.')


def initialise_board():
    """
    Sets all elements of the board to a single space ' '.

    Parameter: 
        board (list): A 3x3 list that represents the game board.

    Return: single space for every element in the board.
    """
    return [[' ' for col in range(3)] for row in range(3)]

def get_player_move(board):
    """
    Ask the user for the cell to put the X in.

    Parameter: 
        board (list): A 3x3 list that represents the game board.

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
            print("That square is already taken. Please choose another square.")
        except ValueError:
            print("Please enter a valid integer.")
        except IndexError:
            print("That square is not valid. Please choose between 1 and 9.")


def choose_computer_move(board):
    """
    Let the computer chose a random empty cell.

    Parameter: 
        board (list): A 3x3 list that represents the game board.
    
    Return: row, col
    """
    print("Computer is choosing a move....")
    available_moves = [(r,c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    if available_moves:
        return random.choice(available_moves)
    return None, None


def check_for_win(board, mark):
    """
    Checks if a player (represented by 'mark') has won the game.

    Parameter: 
        board (list): A 3x3 list that represents the game board.
        mark (str): The player's mark ('X' or 'O').

    Return:
        bool: True if the player has won, False otherwise.
    """
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
    """
    Checks if the game is a draw (i.e., no empty spaces left on the board).

    Parameter: 
        board (list): A 3x3 list that represents the game board.

    Return:
        bool: True if the game is a draw, False otherwise.
    """
    return all(cell != ' ' for row in board for cell in row)


def play_game(board):
    """
    Runs the main game loop where player and computer plays turn by turn.

    Parameter: 
        board (list): A 3x3 list that represents the game board.

    Return: 
        int: 1 if the player wins, -1 if the computer wins, 0 if it's a draw.
    """
    board = initialise_board()
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
    """
    Display menu where user chooses what to perform
                1. Play
                2. Save
                3. Display score
                4. quit 

    Return:
        str: The user's choice.
    """
    choice = input(
        "Choose an option:\n" \
        "1 - Play the game\n" \
        "2 - Save score\n" \
        "3 - Load and display the scores \n" \
        "q - Quit\n Your Choice: ")
    return choice


def load_scores():
    """
    Load and return the leaderboard data from a file named leaderboard.txt.

    Return:
        dict: The leaderboard data as a dictionary.
        {} if the file doesn't exist or is corrupted.
    """
    if not os.path.exists('leaderboard.txt'):
        return {}
    try:
        with open('leaderboard.txt', 'r', encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return {}


def save_score():
    """
    Save the player's score to the leaderboard file.
    """
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = leaders.get(name, 0) + 1
    with open('leaderboard.txt', 'w', encoding='utf-8') as file:
        json.dump(leaders, file)


def display_leaderboard(leaders):
    """
    Display the leaderboard sorted by scores in descending order.

    Parameter:
        leaders (dict): The leaderboard data as a dictionary.
    """
    print("\nLeaderboard:")
    for name, score in sorted(leaders.items(), key=lambda item: item[1], reverse=True):
        print(f"{name}: {score}")

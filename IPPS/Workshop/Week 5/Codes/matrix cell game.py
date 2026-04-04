name = "Sagar Mishra"
print(name)
#program
def play_game():
    matrix = [[1]*3 for _ in range(3)]
    selected = 0
    def current_matrix():
        for row in matrix:
            print(row)
        print()
    print("Welcome to the 3x3 cell selection game!")
    print("Enter row and column values between 0 and 2.\n")
    current_matrix()
    while selected < 9:
        row = input("Row (0-2): ")
        column = input("Column (0-2): ")
        if not (row.isdigit() and column.isdigit()):
            print("Please enter numbers only.\n")
            continue
        row, column = int(row), int(column)
        if row not in range(3) or column not in range(3):
            print("Index out of range!\n")
            continue
        if matrix[row][column] == 'X':
            print("Cell already selected!\n")
            continue
        matrix[row][columnn] = 'X'
        selected += 1
        current_matrix()
    print(f"Game Over! All cells selected in {selected} moves.")
play_game()

# Video alternative: https://vimeo.com/954334009/67af9910fc#t=1054

# So far you've spent a lot of time writing new programs.

# This is great for learning the fundamentals of code, but
# actually isn't very realistic. Most software engineers
# spend their time modifying and maintaining existing
# programs, not writing entirely new ones.

# Below is the same program as in the example. Your
# challenge is to implement some improvements:

# 1. Right now users can place their tiles over the other
#    user's tiles. Prevent this.

# 2. Right now if the game reaches a draw with no more free
#    spaces, the game doesn't end. Make it end at that
#    point.

# 3. If you want a real challenge, try to rework this
#    program to support a 5x5 board rather than a 3x3 board.

# 4. If you're still not satisfied, try to rework this
#    program to take a parameter `board_size` and play a
#    game with a board of that size.

# This is getting really challenging now — and is entirely
# optional. Don't forget about your assessment!

def play_game(board_size):
    # create the board
    board = create_board(board_size)
    # set player
    player = "X"
    while not is_game_over(board, player):
        print(print_board(board))
        print("It's " + player + "'s turn.")
        # get move coordinates
        row, column = get_coords()
        board, updated = make_move(board, row, column, player)
        # check if the board was updated on the last move
        while not updated:
            print(f"({row}, {column}) already taken, try again!")
            row, column = get_coords()
            board, updated = make_move(board, row, column, player)
        player = set_player(player)
    print(print_board(board))
    print("Game over!")


def create_board(board_size):
    board = []
    # create a row list for each row and append "." equal to number of columns
    for _ in range(board_size):
        row = []
        for _ in range(board_size):
            row.append(".")
        board.append(row)
    return board


def print_board(board):
    formatted_rows = []
    for row in board:
        formatted_rows.append(" ".join(row))
    grid = "\n".join(formatted_rows)
    return grid


def get_coords():
    # `input` asks the user to type in a string
    # We then need to convert it to a number using `int`
    row = int(input("Enter a row: "))
    column = int(input("Enter a column: "))
    return row, column


def set_player(player):
    if player == "X":
        return "O"
    return "X"


def make_move(board, row, column, player):
    # only allow move if square not taken
    if board[row][column] == ".":
        board[row][column] = player
        return board, True
    return board, False


def generate_groups(board):
    n = len(board)
    m = len(board[0])
    groups = []
    # create horizontal groups
    x = 0
    y = 0
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append((x, y))
            y += 1
        x += 1
        y = 0
        groups.append(row)

    # create vertical groups
    x = 0
    y = 0
    for _ in range(m):
        column = []
        for _ in range(n):
            column.append((x, y))
            x += 1
        x = 0
        y += 1
        groups.append(column)

    # create diagonal groups
    main_diagonal = []
    anti_diagonal = []
    for i in range(n):
        main_diagonal.append((i, i))
        anti_diagonal.append((i, n - 1 - i))
    groups.append(main_diagonal)
    groups.append(anti_diagonal)
    return groups


def is_group_complete(board, group):
    # This function will check if the group is fully placed
    # with player marks, no empty spaces.
    for coords in group:
        if board[coords[0]][coords[1]] == ".":
            return False
    return True


def are_all_cells_the_same(board, group):
    # This function will check if the group is all the same
    first_set = group[0]
    value = board[first_set[0]][first_set[1]]
    for coords in group:
        if board[coords[0]][coords[1]] != value:
            return False
    return True


def board_full(board):
    # search matrix for a blank space
    for i, _ in enumerate(board):
        for j, _ in enumerate(board[0]):
            if board[i][j] == ".":
                return False
    return True


def is_game_over(board, player):
    # We go through our groups
    for group in generate_groups(board):
        # If any of them are empty, they're clearly not a winning row, so we skip them
        if is_group_complete(board, group):
            if are_all_cells_the_same(board, group):
                print("================")
                print(f"{player} is the winner!")
                print("================")
                return True  # We found a winning row!
        # Note that return also stops the function
    # if the board is full it is also game over
    if board_full(board):
        return True
    return False  # If we get here, we didn't find a winning row

# And test it out:


if __name__ == "__main__":
    print("Game time!")
    print("How many rows and columns do you want in the board?")
    board_size = int(input("Board size: "))
    while board_size < 3:
        print("3 rows x columns is the minimum!")
        print("How many rows and columns do you want in the board?")
        board_size = int(input("Board size: "))
    play_game(board_size)

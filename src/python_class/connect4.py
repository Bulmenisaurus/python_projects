BOARD = [
    [],  # each sub-list is a column
    [],
    [],
    [],
    [],
    [],
    [],
]


# Dimensions: 6 * 7

def pad(to_pad: list) -> list:
    pad_amount = 6
    # the line below is yoinked somewhere from stackoverflow.com
    return [''] * (pad_amount - len(to_pad)) + to_pad


def drop_piece(board: list, column: int, player: str, retry_text: str) -> list:
    """
    Appends a players move the the specified column, with some basic error catching

    :param board: 6 by x matrix that represents the board in play
    :param column: The column by which to drop a players piece. Starts at 1
    :param player: The string by which to represent the person or program moving
    :param retry_text: The text passed to input if the move cant happen for whatever reason
    :return: the updated board
    """
    column -= 1
    if -1 < int(column) < 7:  # if the chosen row is 1, 2, 3, 4, 5, 6, or 7
        if len(board[column]) < 8:  # if the column isn't already full of pieces
            board[column].append(player)  # append the 'piece' to the correct column
            return board
        else:
            print('That column is already full!')
    else:
        print(f':/ {column} is not a valid column! Make sure it is one of the following: {tuple(range(1, 8))}')

    drop_piece(board, int(input(retry_text)), player, retry_text)


def draw_board(board: list, players_fill_char: dict, include_column_names=True) -> str:
    board = list(map(pad, board))  # make all columns 6 tall

    # turn a list of columns into a list of rows (easier to draw)
    # yoinked from https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
    to_rows = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    assert len(to_rows) == 6

    grid = f"┌{'───┬' * 6}───┐\n"
    for row in to_rows:
        grid += '├' + '┼'.join([(players_fill_char.get(item, ' ')).center(3) for item in row]) + '┤\n'

    bottom_joiners = ['┟' if include_column_names else '└',
                      '╁' if include_column_names else '┴',
                      '┧' if include_column_names else '┘']

    grid += f"{bottom_joiners[1]}{f'───{bottom_joiners[1]}' * 6}───{bottom_joiners[2]}\n"
    if include_column_names:
        grid += '║ ' + ' ║ '.join(map(chr, range(65, 72))) + ' ║'
    return grid

def check_wins(board):
    for column in board:
        if repr(column)

player = True
while True:
    print(draw_board(BOARD, {'1': 'X', '0': 'O'}))
    column = input(f'\nWhat column would you like to drop your piece down, player {int(player)}?\n')[0].upper()
    drop_piece(BOARD,             # the board
               ord(column) - 64,  # turns `A` into 1, `B` into 2, etc
               str(int(player)),
               f'Whoops! That didn\'t work! Try again, player {int(player)}')

    player = not player

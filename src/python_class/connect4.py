BOARD = [
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
]


# Dimensions: 6 * 7


def drop_piece(board: list, column: int, player: str, retry_text):
    """
    Appends a players move the the specified column, with some basic error catching

    :param board: 6 by x matrix that represents the board in play
    :param column: The column by which to drop a players piece. Starts at 1
    :param player: The string by which to represent the person or program moving
    :param retry_text: The text passed to input if the move cant happen for whatever reason
    :return: the updated board
    """
    if 0 < int(column) < 7:  # if the chosen row is 1, 2, 3, 4, 5, 6, or 7
        if len(board[column]) < 8:  # if the column isn't already full of pieces
            board[column].append(player)  # append the 'piece' to the correct column
            return board
        else:
            print('That column is already full!')
    else:
        print(f':/ {column} is not a valid column! Make sure it is one of the following: {tuple(range(1, 8))}')

    drop_piece(board, int(input(retry_text)), player, retry_text)


def draw_board(board: list, players_fill_char: dict):
    # yoinked from https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
    to_rows = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    print(to_rows)


draw_board([['a', 'b', 'c'], ['alpha', 'beta', 'gamma'], ['1', '2', '3'], ['Ⅰ', 'Ⅱ', 'Ⅲ'], [''], []], {})

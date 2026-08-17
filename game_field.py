import random

import consts


def create_board():
    board = []
    for _ in range(consts.ROWS_NUM):
        row_cells = []
        for _ in range(consts.COLS_NUM):
            row_cells.append(consts.EMPTY_CELL)
        board.append(row_cells)
    return board


def set_flag_location(board):

    top_row = consts.ROWS_NUM - consts.FLAG_HEIGHT_CELLS
    top_col = consts.COLS_NUM - consts.FLAG_WIDTH_CELLS

    for row in range(top_row, top_row + consts.FLAG_HEIGHT_CELLS):
        for col in range(top_col, top_col + consts.FLAG_WIDTH_CELLS):
            board[row][col] = consts.FLAG_CELL

    return top_row, top_col


def set_landmines_locations(board):

    mines_locations = []

    while len(mines_locations) < consts.MINES_NUM:
        row = random.randint(0, consts.ROWS_NUM - 1)
        col = random.randint(0, consts.COLS_NUM - consts.MINE_WIDTH_CELLS)

        cells = []
        for offset in range(consts.MINE_WIDTH_CELLS):
            cells.append((row, col + offset))

        overlaps = False
        for r, c in cells:
            if board[r][c] != consts.EMPTY_CELL:
                overlaps = True
                break
        if overlaps:
            continue

        for r, c in cells:
            board[r][c] = consts.MINE_CELL
        mines_locations.append((row, col))

    return mines_locations


def is_touching_flag(board, cells):
    for row, col in cells:
        if board[row][col] == consts.FLAG_CELL:
            return True
    return False


def is_touching_mine(board, cells):
    for row, col in cells:
        if board[row][col] == consts.MINE_CELL:
            return True
    return False



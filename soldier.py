import consts


def create_soldier():

    return consts.SOLDIER_START_LOCATION


def clamp_to_board(row, col):

    max_row = consts.ROWS_NUM - consts.SOLDIER_HEIGHT_CELLS
    max_col = consts.COLS_NUM - consts.SOLDIER_WIDTH_CELLS
    row = max(0, min(row, max_row))
    col = max(0, min(col, max_col))
    return row, col


def soldier_move_left(soldier_location):
    row, col = soldier_location
    return clamp_to_board(row, col - 1)


def soldier_move_right(soldier_location):
    row, col = soldier_location
    return clamp_to_board(row, col + 1)


def soldier_move_up(soldier_location):
    row, col = soldier_location
    return clamp_to_board(row - 1, col)


def soldier_move_down(soldier_location):
    row, col = soldier_location
    return clamp_to_board(row + 1, col)


def get_soldier_body_cells(soldier_location):

    row, col = soldier_location
    cells = []
    for r in range(row, row + consts.SOLDIER_BODY_ROWS):
        for c in range(col, col + consts.SOLDIER_WIDTH_CELLS):
            cells.append((r, c))
    return cells


def get_soldier_legs_cells(soldier_location):

    row, col = soldier_location
    legs_row = row + consts.SOLDIER_BODY_ROWS
    # cols_list=[]
    # for i in range(consts.SOLDIER_WIDTH_CELLS):
    #     col=col+i
    #     cols_list.append
    legcells = [(legs_row, col + i) for i in range(consts.SOLDIER_WIDTH_CELLS)]
    return legcells

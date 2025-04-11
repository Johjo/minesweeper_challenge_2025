import pytest


def minesweeper(field: str) -> str:
    solved_field = ""

    if len(field) > 0:
        solved_field += solve_cell(field, 0)

    if len(field) > 1:
        solved_field += solve_cell(field, 1)

    if len(field) > 2:
        solved_field += solve_cell(field, 2)

    return solved_field


def solve_cell(field, x):
    if is_mine(field, x):
        cell = "*"
    else:
        mine_around = 0
        if is_mine(field, x + 1):
            mine_around += 1

        if is_mine(field, x + 1) and is_mine(field, x - 1):
            if is_mine(field, x - 1):
                mine_around += 1
            cell = f"{mine_around}"
        elif is_mine(field, x + 1):
            if is_mine(field, x - 1):
                mine_around += 1
            cell = f"{mine_around}"
        elif is_mine(field, x - 1):
            if is_mine(field, x - 1):
                mine_around += 1
            cell = f"{mine_around}"
        else:
            if is_mine(field, x - 1):
                mine_around += 1
            cell = f"{mine_around}"
    return cell


def is_mine(field, x):
    if is_cell_outside(field, x):
        return False

    return field[x] == "*"


def is_cell_outside(field, x):
    cell_is_outside = False
    if not len(field) > x:
        cell_is_outside = True
    if not x >= 0:
        cell_is_outside = True
    return cell_is_outside


@pytest.mark.parametrize("field, expected", [
    ["", ""],
    [".", "0"],
    ["..", "00"],
    ["...", "000"],
    ["*", "*"],
    ["**", "**"],
    ["***", "***"],
    [".*", "1*"],
    ["..*", "01*"],
    ["*.", "*1"],
    ["*.*", "*2*"],
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected
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
        if is_mine(field, x + 1):
            cell = "1"
        elif is_mine(field, x - 1):
            cell = "1"
        else:
            cell = "0"
    return cell


def is_mine(field, x):
    if not len(field) > x:
        return False

    if not x  >= 0:
        return False

    return field[x] == "*"


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
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected
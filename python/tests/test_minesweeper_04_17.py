import pytest


def minesweeper(field: str) -> str:
    solved_field = ""

    x = 0
    while len(field) > x:
        solved_field += solve_cell(field, x)
        x += 1

    return solved_field


def solve_cell(field, x):
    if is_mine(field, x):
        return "*"
    if is_mine(field, x + 1):
        mine_around = 0
        if is_mine(field, x - 1):
            mine_around += 1
            mine_around += 1
            return f"{mine_around}"
        mine_around += 1
        return f"{mine_around}"
    if is_mine(field, x - 1):
        mine_around = 0
        mine_around += 1
        return f"{mine_around}"
    mine_around = 0
    return f"{mine_around}"


def is_mine(field, x):
    if x < 0:
        return False
    if len(field) == x:
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
    ["*.", "*1"],
    ["*.*", "*2*"],
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected



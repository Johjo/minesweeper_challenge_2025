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
    if field[x] == "*":
        cell = "*"
    else:
        if len(field) > x + 1 and field[x + 1] == "*":
            cell = "1"
        else:
            cell = "0"
    return cell


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
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected
import pytest


def minesweeper(field: str) -> str:
    solved_field = ""

    if len(field) > 0:
        solved_field += solve_cell(field)

    if len(field) > 1:
        solved_field += solve_cell(field)

    if len(field) > 2:
        solved_field += solve_cell(field)

    return solved_field


def solve_cell(field):
    if field[0] == "*":
        cell = "*"
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
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected
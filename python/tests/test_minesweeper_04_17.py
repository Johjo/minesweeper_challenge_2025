import pytest


def minesweeper(field: str) -> str:
    solved_field = ""

    x = 0
    while len(field) > x:
        solved_field += solve_cell(field)
        x += 1

    return solved_field


def solve_cell(field):
    return "0"


@pytest.mark.parametrize("field, expected", [
    ["", ""],
    [".", "0"],
    ["..", "00"],
    ["...", "000"],
    # ["*", "*"],
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected



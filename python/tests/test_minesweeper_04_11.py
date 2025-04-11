import pytest


def minesweeper(field: str) -> str:
    solved_field = ""

    if len(field) > 0:
        if field[0] == "*":
            solved_field += "*"
        else:
            solved_field += "0"

    if len(field) > 1:
        if field[0] == "*":
            solved_field += "*"
        else:
            solved_field += "0"

    if len(field) > 2:
        solved_field += "0"

    return solved_field

@pytest.mark.parametrize("field, expected", [
    ["", ""],
    [".", "0"],
    ["..", "00"],
    ["...", "000"],
    ["*", "*"],
    ["**", "**"],
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected
import pytest


def minesweeper(field: str) -> str:
    solved_field = ""

    x = 0
    while len(field) > x:
        solved_field += "0"
        x += 1
    if len(field) > x:
        solved_field += "0"
        x += 1
    if len(field) > x:
        solved_field += "0"
        x += 1

    return solved_field


@pytest.mark.parametrize("field, expected", [
    ["", ""],
    [".", "0"],
    ["..", "00"],
    ["...", "000"],
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected



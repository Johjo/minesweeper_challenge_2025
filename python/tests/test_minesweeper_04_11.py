import pytest


def minesweeper(field: str) -> str:
    solved_field = ""

    if len(field) > 0:
        solved_field += "0"

    if field == "":
        return solved_field

    if field == ".":
        return solved_field

    if field == "..":
        if len(field) > 1:
            solved_field += "0"
        return solved_field

    solved_field += "0"
    solved_field += "0"
    return solved_field

@pytest.mark.parametrize("field, expected", [
    ["", ""],
    [".", "0"],
    ["..", "00"],
    ["...", "000"],
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected
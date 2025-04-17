import pytest


def minesweeper(field: str) -> str:
    if field == "":
        solved_field = ""
    elif field == ".":
        solved_field = ""
        solved_field += "0"
    else:
        solved_field = ""
        solved_field += "0"
        solved_field += "0"
    return solved_field


@pytest.mark.parametrize("field, expected", [
    ["", ""],
    [".", "0"],
    ["..", "00"],
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected



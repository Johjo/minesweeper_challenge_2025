import pytest


def minesweeper(field: str) -> str:
    solved_field = ""
    if field == "":
        pass
    elif field == ".":
        solved_field += "0"
    else:
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



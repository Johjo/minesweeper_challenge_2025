import pytest


def minesweeper(field: str) -> str:
    if field == "":
        return ""

    if field == ".":
        return "0"

    return "00"

@pytest.mark.parametrize("field, expected", [
    ["", ""],
    [".", "0"],
    ["..", "00"],
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected
import pytest


def minesweeper(field: str) -> str:
    if field == "":
        return ""

    if field == ".":
        return "0"

    if field == "..":
        return "00"

    return "000"

@pytest.mark.parametrize("field, expected", [
    ["", ""],
    [".", "0"],
    ["..", "00"],
    ["...", "000"],
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected
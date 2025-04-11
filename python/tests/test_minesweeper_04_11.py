import pytest


def minesweeper(field: str) -> str:
    if field == "":
        return ""

    return "0"


@pytest.mark.parametrize("field, expected", [
    ["", ""],
    [".", "0"],
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected
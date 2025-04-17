import pytest


def minesweeper(field: str) -> str:
    return ""


@pytest.mark.parametrize("field, expected", [
    ["", ""]])
def test_minesweeper(field, expected):
    assert minesweeper("") == ""



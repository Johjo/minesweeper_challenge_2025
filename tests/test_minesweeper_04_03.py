# for the mine field : . the solved mine field is 0
# for the mine field : * the solved mine field is *
# for the mine field : .. the solved mine field is 00
# for the mine field : ** the solved mine field is **
# for the mine field : .* the solved mine field is 1*
# for the mine field : *. the solved mine field is *1
# for the mine field : ... the solved mine field is 000
# for the mine field : ..* the solved mine field is 01*
# for the mine field : *.. the solved mine field is *10
# for the mine field : *.* the solved mine field is *2*
# for the mine field : .*. the solved mine field is 1*1
import pytest


def minesweeper(field):
    if field == "..":
        return solve_cell(field, 0) + solve_cell(field, 1)
    if len(field) == 1:
        return solve_cell(field, 0)
    return ""

def solve_cell(field, x):
    if field[x] == ".":
        return "0"
    if field[x] == "*":
        return "*"


@pytest.mark.parametrize("field, expected", [
    ["", ""],
    [".", "0"],
    ["*", "*"],
    ["..", "00"],

])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected
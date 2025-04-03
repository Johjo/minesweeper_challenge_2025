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
    return ""


@pytest.mark.parametrize("field, expected", [
    ["", ""],
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected
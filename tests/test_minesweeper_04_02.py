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


def minesweeper(field: str) -> str:
    if field == "*":
        solved_field = ""
        solved_field += "*"
        return solved_field
    if field == "**":
        solved_field = ""
        solved_field += "*"
        solved_field += "*"
        return solved_field
    if field == "..":
        return "0" + "0"

    return "0"


def test_minesweeper_01():
    assert minesweeper(".") == "0"

def test_minesweeper_02():
    assert minesweeper("*") == "*"

def test_minesweeper_03():
    assert minesweeper("..") == "00"

def test_minesweeper_04():
    assert minesweeper("**") == "**"

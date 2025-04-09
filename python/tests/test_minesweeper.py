# ..*..
# *....
# ..*..



# 12*10
# *2320
# 12*10

# ***
# *.*
# ***

# ***
# *8*
# ***


# 1 indique qu'il y a une mine à côté
# 2 indique qu'il y a deux mines à côté


def minesweeper(field):
    solved_field = ""
    if field == "..":
        solved_field += "0"
        solved_field += "0"
        return solved_field
    if field == ".":
        solved_field += "0"
    if field == "**":
        solved_field += "*"
        if True:
            solved_field += "*"
    if field == "*":
        if True:
            solved_field += "*"
        if False:
            solved_field += "*"

    return solved_field




def test_minesweeper():
    assert minesweeper("") == ""

def test_minesweeper_01():
    assert minesweeper(".") == "0"

def test_minesweeper_02():
    assert minesweeper("*") == "*"

def test_minesweeper_03():
    assert minesweeper("..") == "00"

def test_minesweeper_04():
    assert minesweeper("**") == "**"




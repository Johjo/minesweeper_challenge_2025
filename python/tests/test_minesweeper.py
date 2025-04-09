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
    solvedField = ""
    if field == "..":
        solvedField += "0"
        solvedField += "0"
        return solvedField
    if field == ".":
        solvedField += "0"
        return solvedField
    if field == "*":
        solvedField += "*"
        return solvedField
    return ""




def test_minesweeper():
    assert minesweeper("") == ""

def test_minesweeper_01():
    assert minesweeper(".") == "0"

def test_minesweeper_02():
    assert minesweeper("*") == "*"

def test_minesweeper_03():
    assert minesweeper("..") == "00"




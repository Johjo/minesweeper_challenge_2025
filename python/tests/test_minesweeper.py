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

    if field == "":
        if len(field) == 1:
            solved_field += "*"


    if field == "*":
        if len(field) >= 1:
            solved_field += "*"

    if field == "**":
        if len(field) >= 1:
            solved_field += "*"

    if len(field) == 2:
        solved_field += "*"



    return solved_field




def test_minesweeper():
    assert minesweeper("") == ""


def test_minesweeper_02():
    assert minesweeper("*") == "*"


def test_minesweeper_04():
    assert minesweeper("**") == "**"






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
    if "." in field:
        solved_field = ""

        x = 0
        while len(field) > x:
            if field[0] == ".":
                solved_field += "0"
            if False:
                solved_field += "*"

            x += 1

        return solved_field


    solved_field = ""

    x = 0
    while len(field) > x:
        if field[0] == ".":
            solved_field += "0"
        if True:
            solved_field += "*"
        x += 1

    return solved_field


def test_minesweeper():
    assert minesweeper("") == ""


def test_minesweeper_02():
    assert minesweeper("*") == "*"


def test_minesweeper_04():
    assert minesweeper("**") == "**"


def test_minesweeper_05():
    assert minesweeper("***") == "***"

def test_minesweeper_06():
    assert minesweeper(".") == "0"

def test_minesweeper_07():
    assert minesweeper("..") == "00"





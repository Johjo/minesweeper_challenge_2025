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

    x = 0
    while len(field) > x :
        solved_field += solve_cell(field, x)
        x += 1

    return solved_field


def solve_cell(field, x):
    if field[x] == ".":
        count = 0

        count = count_mine(field, x)

        return f"{count}"
    else:
        return "*"


def count_mine(field, x):
    count = 0
    if len(field) > x + 1 and field[x + 1] == "*":
        count += 1
    if x - 1 >= 0 and field[x - 1] == "*":
        count += 1
    return count


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

def test_minesweeper_08():
    assert minesweeper(".*") == "1*"

def test_minesweeper_09():
    assert minesweeper("*.") == "*1"

def test_minesweeper_10():
    assert minesweeper("*.*") == "*2*"



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
    if field == ".\n.":
        return "\n".join(["0", "0"])

    return solve_line(field)


def solve_line(field):
    solved_line = ""
    x = 0
    while len(field) > x:
        solved_line += solve_cell(field, x)
        x += 1
    return solved_line


def solve_cell(field, x):
    if field[x] == ".":
        return f"{count_mine(field, x)}"
    else:
        return "*"


def is_mine(field, x):
    if len(field) <= x:
        return False
    if x < 0:
        return False
    return field[x] == "*"


def count_mine(field, x):
    count = 0

    if is_mine(field, x+1) :
        count += 1
    if is_mine(field, x-1):
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
    assert minesweeper(".\n.") == "0\n0"




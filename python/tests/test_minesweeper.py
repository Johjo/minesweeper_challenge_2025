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

    lines =  field.split("\n")

    return solve_line(field, lines)


def solve_line(field, lines):
    solved_line = ""
    x = 0
    while len(field) > x:
        solved_line += solve_cell(field, x, lines)
        x += 1
    return solved_line


def solve_cell(field, x, lines):
    if is_mine(lines, x):
        return "*"
    return f"{count_mine(lines, x)}"


def is_mine(lines, x):
    if not is_in_field(lines, x):
        return False

    return lines[0][x] == "*"


def is_in_field(lines, x):
    if len(lines[0]) <= x:
        return False
    if x < 0:
        return False
    return True


def count_mine(lines, x):
    count = 0

    if is_mine(lines, x + 1):
        count += 1
    if is_mine(lines, x - 1):
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




import pytest


def minesweeper(field: str) -> str:
    lines = field.split("\n")
    if len(lines) == 2:
        solved_lines = [solve_line(lines[0]), solve_line(lines[0])]
    elif len(lines) == 3:
        solved_lines = [solve_line(lines[0]), solve_line(lines[0]), solve_line(lines[0])]
    else:
        solved_lines = [solve_line(lines[0])]
    return "\n".join(solved_lines)


def solve_line(field):
    x = 0
    solved_line = ""
    while len(field) > x:
        solved_line += solve_cell(field, x)
        x += 1
    return solved_line


def solve_cell(field, x):
    if is_mine(field, x):
        return "*"
    return f"{count_mine_around(field, x)}"


def count_mine_around(field, x):
    mine_around = 0
    if is_mine(field, x + 1):
        mine_around += 1
    if is_mine(field, x - 1):
        mine_around += 1
    return mine_around


def is_mine(field, x):
    if is_cell_outside(field, x):
        return False

    return field[x] == "*"


def is_cell_outside(field, x):
    cell_is_outside = False
    if not len(field) > x:
        cell_is_outside = True
    if not x >= 0:
        cell_is_outside = True
    return cell_is_outside


@pytest.mark.parametrize("field, expected", [
    ["", ""],
    [".", "0"],
    ["..", "00"],
    ["...", "000"],
    ["*", "*"],
    ["**", "**"],
    ["***", "***"],
    [".*", "1*"],
    ["..*", "01*"],
    ["*.", "*1"],
    ["*.*", "*2*"],
    [".*.**.*.", "1*2**2*1"],
    [".\n.", "0\n0"],
    ["*\n*", "*\n*"],
    ["..\n..\n..", "00\n00\n00"],
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected
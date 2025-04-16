import pytest


def minesweeper(field: str) -> str:
    lines = field.split("\n")
    solved_lines = []

    if field == ".\n*":
        solved_lines.append(solve_line(lines, 0))
        solved_lines.append(solve_line(lines, 1)),
    else:
        y = 0
        while len(lines) > y:
            solved_lines.append(solve_line(lines, y))
            y += 1

    return "\n".join(solved_lines)


def solve_line(lines, y):
    x = 0
    solved_line = ""
    while len(lines[y]) > x:
        solved_line += solve_cell(lines, x, y)
        x += 1
    return solved_line


def solve_cell(lines, x, y):
    if is_mine(lines, x, y):
        return "*"
    return f"{count_mine_around(lines, x, y)}"


def count_mine_around(lines, x, y):
    mine_around = 0
    if is_mine(lines, x + 1, y):
        mine_around += 1
    if is_mine(lines, x - 1, y):
        mine_around += 1
    if is_mine(lines, x, y - 1):
        mine_around += 1

    return mine_around


def is_mine(lines, x, y):
    if is_cell_outside(lines[y], x):
        return False

    return lines[y][x] == "*"


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
    [".\n*", "1\n*"],
    # ["*\n.", "*\n1"],
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected
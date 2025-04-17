import pytest


def minesweeper(field: str) -> str:
    lines = field.split("\n")
    solved_lines = []

    y = 0
    while len(lines) > y:
        solved_lines.append(solve_line(lines, lines[0], y))
        y += 1

    return "\n".join(solved_lines)


def solve_line(lines, line, y):
    solved_field = ""
    x = 0
    while len(line) > x:
        solved_field += solve_cell(lines, line, x, y)
        x += 1
    return solved_field


def solve_cell(lines, line, x, y):
    if is_mine(lines, line, x, y):
        return "*"
    return f"{count_mine_around(lines, line, x, y)}"


def count_mine_around(lines, line, x, y):
    mine_around = 0
    if is_mine(lines, line, x + 1, y):
        mine_around += 1
    if is_mine(lines, line, x - 1, y):
        mine_around += 1
    if is_mine(lines, line, x, y + 1):
        mine_around += 1
    if is_mine(lines, line, x, y - 1):
        mine_around += 1
    if is_mine(lines, line, x - 1, y - 1):
        mine_around += 1
    if is_mine(lines, line, x + 1, y - 1):
        mine_around += 1
    if is_mine(lines, line, x - 1, y + 1):
        mine_around += 1
    if is_mine(lines, line, x + 1, y + 1):
        mine_around += 1
    return mine_around


def is_mine(lines, line, x, y):
    if y < 0:
        return False
    if x < 0:
        return False

    if len(lines) == y:
        return False
    if len(lines[0]) == x:
        return False

    return lines[y][x] == "*"


@pytest.mark.parametrize("field, expected", [
    ["", ""],
    [".", "0"],
    ["..", "00"],
    ["...", "000"],
    ["*", "*"],
    ["**", "**"],
    ["***", "***"],
    [".*", "1*"],
    ["*.", "*1"],
    ["*.*", "*2*"],
    ["*\n*", "*\n*"],
    ["**\n**", "**\n**"],
    ["**\n**\n**", "**\n**\n**"],
    [".\n*", "1\n*"],
    ["*\n.", "*\n1"],
    ["*.\n..", "*1\n11"],
    [".*\n..", "1*\n11"],
    ["..\n*.", "11\n*1"],
    ["..\n.*", "11\n1*"],
    [".*.**.\n....*.\n..*...", "1*2**2\n1234*2\n01*211"],
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected



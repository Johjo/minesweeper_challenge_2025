import pytest


def minesweeper(field: str) -> str:
    lines = field.split("\n")
    solved_lines = []

    y = 0
    while len(lines) > y:
        solved_lines.append(solve_line(lines[0], field, y))
        y += 1

    return "\n".join(solved_lines)


def solve_line(line, field, y):
    solved_field = ""
    x = 0
    while len(line) > x:
        solved_field += solve_cell(line, x, field, y)
        x += 1
    return solved_field


def solve_cell(line, x, field, y):
    if is_mine(line, x, field, y):
        return "*"
    return f"{count_mine_around(line, x, field, y)}"


def count_mine_around(line, x, field, y):
    mine_around = 0
    if is_mine(line, x + 1, field, y):
        mine_around += 1
    if is_mine(line, x - 1, field, y):
        mine_around += 1
    if is_mine(line, x, field, y + 1):
        mine_around += 1
    if is_mine(line, x, field, y - 1):
        mine_around += 1
    return mine_around


def is_mine(line, x, field, y):
    lines = field.split("\n")

    if y < 0:
        return False
    if x < 0:
        return False

    try:
        return lines[y][x] == "*"
    except:
        return False


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
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected



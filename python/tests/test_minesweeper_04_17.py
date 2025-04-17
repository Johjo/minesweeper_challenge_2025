import pytest


def minesweeper(field: str) -> str:
    lines = field.split("\n")
    solved_lines = []

    y = 0
    if len(lines) > y:
        solved_lines.append(solve_line(lines[0]))
        y += 1
    if len(lines) > y:
        solved_lines.append(solve_line(lines[0]))
        y += 1
    if len(lines) > y:
        solved_lines.append(solve_line(lines[0]))
        y += 1

    return "\n".join(solved_lines)


def solve_line(line):
    solved_field = ""
    x = 0
    while len(line) > x:
        solved_field += solve_cell(line, x)
        x += 1
    return solved_field


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
    if x < 0:
        return False
    if len(field) == x:
        return False
    return field[x] == "*"


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
])
def test_minesweeper(field, expected):
    assert minesweeper(field) == expected



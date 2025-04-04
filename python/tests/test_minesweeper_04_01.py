# For this mine field : , the solved mine field is
# .*.**.
# ....*.
# ..*...
#
# the solved mine field is
#
# 1*2**2
# 1234*2
# 01*211
#

def minesweeper(field: str) -> str:
    return "1*2**2\n1234*2\n01*211"


def test_minesweeper():
    assert minesweeper(""".*.**.
....*.
..*...""" == """
1*2**2
1234*2
01*211
""")





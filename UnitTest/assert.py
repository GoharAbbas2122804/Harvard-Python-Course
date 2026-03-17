import sys
sys.path.append('../Libraries')
from MathLib import Square

def test_Square():
    assert Square(2) == 4
    try:
        assert Square(-3) == 9
    except AssertionError:
        print("Test failed for Square(-3)")
    assert Square(0) == 0
    try:
        assert Square(1.5) == 2.25
    except AssertionError:
        print("Test failed for Square(1.5)")
test_Square()
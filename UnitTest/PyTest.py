import sys
sys.path.append('../Libraries')
from MathLib import Square
from MathLib import EvenOddCheck

def test_Square():
    assert Square(2) == 4
    assert Square(4) == 16

def test_negative():    
    assert Square(-3) == 9

def test_zero():
    assert Square(0) == 0 
    print("*****All test Passed *****")


# n = int(input("Enter a Number: "))
# EvenOddCheck(n)


test_Square()
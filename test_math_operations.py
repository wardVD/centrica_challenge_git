# test_math_operations.py
from ops import add_numbers, square_number, substract_numbers


def test_add():
    assert add_numbers(3, 5) == 8
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_subtract():
    assert substract_numbers(5, 3) == 2
    assert substract_numbers(1, -1) == 2
    assert substract_numbers(0, 0) == 0


def test_square_number():
    assert square_number(5) == 25
    assert square_number(-5) == 25

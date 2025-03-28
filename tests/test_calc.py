import pytest
from calc import calculate

def test_addition():
    assert calculate(5, 3, 1) == ("сложения", 8)

def test_subtraction():
    assert calculate(10, 4, 2) == ("вычитания", 6)

def test_division():
    assert calculate(8, 2, 3) == ("деления", 4.0)

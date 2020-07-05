import pytest
from package.bisection import bisection

def test_bisection():
    assert bisection(1.0, 2.0, 50) == 1.36517333984375

def test_bisection_invalid_a():
    with pytest.raises(Exception):
        bisection(0, 2.0, 50)

def test_bisection_invalid_b():
    with pytest.raises(Exception):
        bisection(1.0, 0, 50)

def test_bisection_invalid_iterations():
    with pytest.raises(Exception):
        bisection(1.0, 2.0, 50.0)

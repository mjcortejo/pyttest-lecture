import pytest
from package.factorial import factorial

def test_factorial():
    assert factorial(4) == 24, "expected output, 24"

def test_factorial_invalid_input():
    with pytest.raises(Exception):
        factorial("hello")

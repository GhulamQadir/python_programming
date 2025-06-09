from calculator import Calculator
import pytest


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(6, 7) == 13


def test_subtract(calc):
    assert calc.subtract(2, 7) == -5


def test_multiply(calc):
    assert calc.multiply(3, 4) == 12


def test_divide(calc):
    assert calc.divide(20, 4) == 5


def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(5, 0)


if __name__ == "__main__":
    pytest.main(["-v", __file__])

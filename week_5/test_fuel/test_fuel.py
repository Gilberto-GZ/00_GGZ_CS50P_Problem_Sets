import pytest
from fuel import convert
from fuel import gauge

def main():
    test_convert_fraction()
    test_value_error()
#Test common fractions
def test_convert_fraction():
    assert convert("3/4") == 75 and gauge(75) == "75%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

if __name__ == "__main__":
    main()
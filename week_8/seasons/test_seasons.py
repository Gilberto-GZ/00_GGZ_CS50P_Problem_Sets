import pytest

from seasons import birthday

def main():

    test_1()
    test_2()


def test_1():
    assert birthday(2022, 5, 1) == birthday(2022, 5, 1)
    assert birthday(2021, 5, 1) == birthday(2021, 5, 1)

if __name__ == "__main__":
    main()
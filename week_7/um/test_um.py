from um import count
import pytest

def main():
    test_count()
    test_case()


def test_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um, thankd for the album.") == 1
    assert count("um, thanks, um...") == 2

def test_case():
    assert count("um") == 1
    assert count("Um") == 1

if __name__ == "__main__":
    main()
from plates import is_valid

def main():
    test_plate_startwith()
    test_plate_length()
    test_plate_numbers()
    test_zero_in_plates()
    test_punctuation_in_plates()

def test_plate_startwith():
    assert is_valid('ABCDEF') == True
    assert is_valid('0ABCDE') == False
    assert is_valid('A1ABCD') == False
    assert is_valid('11ABCD') == False

def test_plate_length():
    assert is_valid('ABCDEF') == True
    assert is_valid('ABCDE') == True
    assert is_valid('ABC') == True
    assert is_valid('AB') == True
    assert is_valid('A') == False

def test_plate_numbers():
    assert is_valid('ABC123') == True
    assert is_valid('ABCD12') == True
    assert is_valid('ABCDE1') == True
    assert is_valid('AB12EF') == False
    assert is_valid('ABC12F') == False
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False
    assert is_valid(" 1") == False

def test_zero_in_plates():
    assert is_valid('ABC102') == True
    assert is_valid('CS50') == True
    assert is_valid('ABC012') == False
    assert is_valid('ABCD01') == False

def test_punctuation_in_plates():
    assert is_valid('ABC.23') == False
    assert is_valid('ABC 23') == False
    assert is_valid('ABC,12') == False
    assert is_valid('AB:12') == False
    assert is_valid('AB/12') == False

if __name__ == "__main__":
    main()
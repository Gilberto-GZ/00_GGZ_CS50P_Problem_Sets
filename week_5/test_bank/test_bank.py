from bank import value

def main():
    #Call test functions
    test_value()

#Test value
def test_value():
    assert value("Hello") == 0
    assert value("Hey") == 20
    assert value("whats'up") == 100

if __name__ == "__main__":
    main()
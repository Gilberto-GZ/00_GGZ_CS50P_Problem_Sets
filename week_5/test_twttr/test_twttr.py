from twttr import shorten

def main():
    #Call test functions
    test_letters()
    test_numbers()
    test_punctuation()

#Test letters
def test_letters():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwiTteR") == "TwTtR"
#Test numbers
def test_numbers():
    assert shorten("1234") == "1234"

#Test punctutation
def test_punctuation():
    assert shorten("!?.,") == "!?.,"

if __name__ == "__main__":
    main()
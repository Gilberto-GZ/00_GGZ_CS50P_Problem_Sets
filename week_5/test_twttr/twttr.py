def main():

    msg = input("Enter your mesage: ")
    print("Output: " + shorten(msg))

def shorten(text):

    vowels = ["a", "e", "i", "o", "u"]
    new_txt = ""

    for i in text:
        if not i.casefold() in vowels:

            new_txt += i


    return new_txt

if __name__ == "__main__":
    main()
def main():

    text = input("Enter your mesage: ")
    print(replaceVowels(text))

def replaceVowels(text):

    vowels = ["a", "e", "i", "o", "u"]
    new_txt = ""

    for i in text:
        if not i.casefold() in vowels:

            new_txt += i
        else:
            pass


    return new_txt

if __name__ == "__main__":
    main()
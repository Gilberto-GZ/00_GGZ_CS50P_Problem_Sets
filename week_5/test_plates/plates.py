def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):


    if s.isalnum() == False or len(s) < 2 or len(s) > 6:
        return False


    for i in range(2):
        if s[i].isalpha() == False:
            return False


    temp = ""
    for i in range(0, len(s)):
        if s[i].isalpha() == False:
            temp += s[i]
            if temp[0] == "0":
                return False


    if s.isalpha():
        return True


    for i in range(0, len(s)):
        if s[i].isalpha() == False:
            recorder = i
            break
    valid = True
    for i in range(recorder, len(s)):
        if s[i].isalpha():
            valid = False

    if valid == False:
        return False
    return True


if __name__ == "__main__":
    main()
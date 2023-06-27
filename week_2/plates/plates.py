def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    nums = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    digits = [x for x in s if x.isdigit()]
    no_allowed = [".", " ", ",", "!", "?","_"]
    while s[0:2].isalpha() and len(s) in range(2, 7):


        if any(x in s for x in no_allowed):

            return False
        if len(digits) != 0:


            if digits[0] == "0":

                return False

            if s.endswith(nums,-1) == False and s.endswith(nums,-2) == False:
                return False


            else:

                return s
        else:
            return s













main()


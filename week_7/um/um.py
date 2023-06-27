import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    p1 = re.compile(r"^([U|u]m\W?)|(\W[U|u]m\W)")
    list = re.findall(p1, s)
    if list:

        count = len(list)
        print(list)
        return count


...


if __name__ == "__main__":
    main()
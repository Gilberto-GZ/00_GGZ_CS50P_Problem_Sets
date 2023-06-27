import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    p1 = re.compile(r"^(\d+):*([0-5][0-9])*( [A-P]M)* to (\d+):*([0-5][0-9])*( [A-P]M)*$")
    format_ok = re.search(p1, s)
    if format_ok:
        sets = format_ok.groups()

        if int(sets[0]) > 12 or int(sets[3]) > 12:
            raise ValueError
        hour = converted_format(sets[0], sets[1], sets[2])
        min = converted_format(sets[3], sets[4], sets[5])
        return hour + ' to ' + min


    else:
        raise ValueError

def converted_format(h, m, xm):
    if xm == ' PM':
        if int(h) == 12:
            converted_h = 12
        else:
            converted_h = int(h) + 12
    else:
        if int(h) == 12:
            converted_h = 0
        else:
            converted_h = int(h)
    if m == None:
        converted_m = ':00'
        converted_time = f"{converted_h:02}" + converted_m
    else:
        converted_time = f"{converted_h:02}" + ":" + m
    return converted_time


if __name__ == "__main__":
    main()
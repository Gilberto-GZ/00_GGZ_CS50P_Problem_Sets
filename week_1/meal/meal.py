def main():

    time = input("What time is it: ")

    if convert(time) >= 7.0 and convert(time) <= 8.0:

        print("breakfast time")

    elif convert(time) >= 12.0 and convert(time) <= 13.0:

        print("lunch time")

    elif convert(time) >= 18.0 and convert(time) <= 19.0:

        print("dinner time")





def convert(time):

    if time.endswith(" a.m.") or time.endswith(" p.m."):

        time = time[:-4]

        hours, minutes = time.split(":")

        convert = float(hours) + float(minutes)/60

        return convert

    else:


        hours, minutes = time.split(":")

        convert = float(hours) + float(minutes)/60

        return convert


if __name__ == "__main__":
    main()
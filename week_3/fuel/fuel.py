while True:

    fraction = input("Enter a fraction: ").split("/")
    try:
        x = int(fraction[0])
        y = int(fraction[1])

        percentage = ((x / y) * 100)
        if percentage <= 1:
            #print("E")
            percentage = "E"
        elif percentage >= 99 and percentage <= 100:
            #print("F")
            percentage = "F"
        elif percentage > 100:
            percentage = 1 / 0
        else:
            percentage = str(round(percentage))+"%"

    except (ValueError, ZeroDivisionError):

        print("No valid fraction")

    else:
        break

print(percentage)



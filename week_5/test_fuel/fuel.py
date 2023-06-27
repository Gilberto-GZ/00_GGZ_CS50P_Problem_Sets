def main():
    fraction = input("Enter a fraction: ")
    #print(fraction)
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:
        fraction = fraction.split("/")

        try:
            x = int(fraction[0])
            y = int(fraction[1])

            percentage = ((x / y) * 100)
            if percentage <= 1:
                return percentage

            elif percentage >= 99 and percentage <= 100:
                return percentage
            elif percentage > 100:
                return percentage
            else:
                return round(percentage)

        except (IndexError, ValueError, ZeroDivisionError):
            raise

def gauge(percentage):


    if percentage <= 1:

        return "E"
    elif percentage >= 99 and percentage <= 100:

        return "F"
    elif percentage > 100:
        return percentage
    else:
        return str(round(percentage))+"%"

if __name__ == "__main__":
    main()

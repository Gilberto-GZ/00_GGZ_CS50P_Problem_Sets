months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    try:

        date = input("Date: ").title()

        if "/" in date:

            date_splitted = date.split("/")
            mm = int(date_splitted[0])
            dd = int(date_splitted[1])
            yy = int(date_splitted[2])

            if dd < 32 and mm < 13:

                print(f'{yy}-{mm:02}-{dd:02}')

                break
        else:

            date_splitted = date.replace(",", "").split()
            str_mm = (date_splitted[0])
            mm = months.index(str_mm) + 1
            dd = int(date_splitted[1])
            yy = int(date_splitted[2])

            if "," in date and dd < 32 and mm < 13:

                print(f'{yy}-{mm:02}-{dd:02}')

                break


    except ValueError:
        pass
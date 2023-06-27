import sys
from tabulate import tabulate
table = []
# total arguments
n = len(sys.argv)
if n < 2:
    sys.exit("Too few command-line arguments")
elif n > 2:
    sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")

else:
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                row = line.replace("\n", "").split(",")
                table.append(row)
            print(table)
            print(tabulate(table, headers="firstrow", tablefmt="grid"))


    except FileNotFoundError:
        sys.exit("File does not exist")
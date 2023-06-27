import sys
import csv
from tabulate import tabulate

list = []

n = len(sys.argv)
if n < 3:
    sys.exit("Too few command-line arguments")
elif n > 3:
    sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")

else:
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name_splitted = row["name"].split(",")

                list.append({"first":name_splitted[1].lstrip(), "last":name_splitted[0].lstrip(), "house":row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first":"first", "last":"last", "house":"house"})

        for row in list:
            writer.writerow({"first":row["first"], "last":row["last"], "house":row["house"]})

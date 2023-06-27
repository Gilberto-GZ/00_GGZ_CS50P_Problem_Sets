import sys
list_lines = []
# total arguments
n = len(sys.argv)
if n < 2:
    sys.exit("Too few command-line arguments")
elif n > 2:
    sys.exit("Too many command-line arguments")
elif ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")

else:
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if len(line.split()) == 0:
                    continue
                if not line.lstrip().startswith("#"):
                    list_lines.append(line)

            print(len(list_lines))
    except FileNotFoundError:
        sys.exit("File does not exist")

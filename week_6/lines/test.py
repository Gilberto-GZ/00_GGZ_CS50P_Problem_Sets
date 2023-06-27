names = []



#with open("names.txt") as file:
    #for line in sorted(file):
        #print("Hello,", line.rstrip())
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names, reverse=True):
    print(f"Hello, {name}")
"""
name = input("What's your name?")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
"""
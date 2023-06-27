camelCase = input("Enter your camelCase text: ")

for i in camelCase:

    if i.isupper():
        a = i.lower()
        b = "_" + a
        i = b

    print(i, end="")
expression = input("Enter your expression: ")

x, y, z = expression.split(" ")

if y == "+":
    print(float(x) + float(z))

elif y == "-":
    print(float(x) - float(z))

elif y == "/":
    print(float(x) / float(z))

else:
    print(float(x) * float(z))

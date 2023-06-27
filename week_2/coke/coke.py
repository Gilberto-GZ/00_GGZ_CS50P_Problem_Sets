i = 0
while i < 50:
    a = int(input("insert coin: "))
    if a == 5 or a == 10 or a == 25:

        i += a

        amount_due = 50 - i
        if amount_due <= 0:
            print("Change Owed: " + str(amount_due).replace("-",""))
        else:
            print("Amount Due: " + str(amount_due))

    else:
        i += 0

        print("Amount Due: " + str(50 - i))



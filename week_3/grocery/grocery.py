d = {}
list = []

while True:
    try:
        item = input().upper().strip()
        list.append(item)

        if item not in d.keys():
            d[item] = 1
        else:
            a = list.count(item)
            d.update({item:a})

    except (EOFError, KeyError, KeyboardInterrupt):
        print()
        break

print("\n".join("{} {}".format(v, k) for k, v in sorted(d.items())))

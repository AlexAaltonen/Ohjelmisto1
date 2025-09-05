number = int(input("Anna kokonaisluku: "))


if number < 2:
    print(f"{number} ei ole alkuluku")
else:
    alkuluku = True

    for i in range(2, number):
        if number % i == 0:
            alkuluku = False
            break
        else:
            alkuluku = True

    if alkuluku:
        print(f"{number} on alkuluku")
    else:
        print(f"{number} ei ole alkuluku")





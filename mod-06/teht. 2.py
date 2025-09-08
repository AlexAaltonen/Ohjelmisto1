import random




def silmanoppa():
    luku = 0
    tahko = int(input("Anna tahkojen määrä: "))
    for i in range(tahko):
        while luku != tahko:
            luku = random.randint(1, tahko)
            print(luku)
        else:
            return

silmanoppa()


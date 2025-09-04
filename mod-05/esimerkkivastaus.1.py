import random

num =int(input("Arpakuutioiden lukumäärä: "))
summa = 0

for i in range(num):
    print("Arpakuutio", i + 1)
    dice_number = random.randint(1, 6)

    print("Tulos: "+ str(random.randint(1, 6)))
    summa+= dice_number

print(f"Noppien summa = {summa}")



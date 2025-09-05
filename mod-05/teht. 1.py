import random

summa = 0

kuutiot = input("Anna arpakuutioiden lukumäärä: ")

for i in range(int(kuutiot)):
    dice = random.randint(1, 6)
    summa += dice
    print("Arpakuutio:", i +1)
    print("tulos:" + str(dice))

print(f"silmälukujen summa: {summa}")


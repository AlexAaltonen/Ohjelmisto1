import random

luku = random.randint(1, 10)
print(luku)

arvaus = input("Arvaa luku 1-10 välilitä: ")

while luku != arvaus:
    if luku > int(arvaus):
        print("luku on suurempi")
        arvaus = input("Arvaa uudestaan: ")

    elif luku < int(arvaus):
        print("luku on pienempi")
        arvaus = input("Arvaa uudestaan: ")
    else:
        print("aivan oikein!")
        break
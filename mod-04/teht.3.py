luku = input("kirjoita luku: ")

pienin = int(luku)
suurin = int(luku)

while luku != "":
    if pienin > int(luku):
        pienin = int(luku)
    if suurin < int(luku):
        suurin = int(luku)
    luku = input("kirjoita luku: ")
else:
    print(f"suurin luku: {suurin}")
    print(f"pienin luku: {pienin}")
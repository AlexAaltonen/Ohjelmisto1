
nimet = set()

nimi = input("kirjoita nimiä, tyhjä lopettaa: ")


while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

    nimi = input("kirjoita nimiä, tyhjä lopettaa: ")

print("Nimet allekkain:")
for alkiot in nimet:
    print(alkiot)


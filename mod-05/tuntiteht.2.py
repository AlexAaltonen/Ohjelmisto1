luvut = []

tulostetut_luvut = []

arvo_str = input("anna luku, tyhjä lopettaa: ")

while arvo_str != "":
    arvo = int(arvo_str)
    luvut.append(arvo)
    arvo_str = input("anna luku, tyhjä lopettaa: ")

for luku in luvut:
    # eikö lukua ole vielä tulostettu
    if luku > 100 and luku not in tulostetut_luvut:
        tulostetut_luvut.append(luku)
        print(luku)

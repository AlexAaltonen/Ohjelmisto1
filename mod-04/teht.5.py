kayttajatunnus = input("kirjoita käyttäjätunnus: ")
salasana = input("kirjoita salasana: " )

kerrat = 0


while kayttajatunnus != "python" and salasana !="rules":
    if kerrat <= 5:
        print("käyttäjätunnus tai salasana väärin")
        kayttajatunnus = input("kirjoita käyttäjätunnus: ")
        salasana = input("kirjoita salasana: ")
        kerrat = kerrat + 1

    else:
        print("pääsy evätty")
        break
print("Tervetuloa!")


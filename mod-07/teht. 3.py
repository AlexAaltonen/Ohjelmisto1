user =input("haluatko syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. (S/H/L): ")

lento_asema = {}

while user !="L":
    if user =="S":
        icao_koodi = input("kirjoita lentoaseman ICAO-koodi: ")
        nimi = input("kirjoita lento-aseman nimen: ")
        lento_asema[icao_koodi]=nimi
        print("lentoasema lisätty")

    if user =="H":
        icao_koodi = input("kirjoita lentoaseman ICAO-koodi: ")
        if icao_koodi in lento_asema:
            print(lento_asema.get(icao_koodi))
        else:
            print("lentoasemaa ei löytynyt")

    user = input("haluatko syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. (S/H/L): ")

print("ohjelma lopetettu.")


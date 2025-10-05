
luvut = []

arvo = int(input("Anna kokonaisluku, 0 lopettaa: "))

while arvo != 0:
    luvut.append(arvo)
    arvo = int(input("Anna kokonaisluku, 0 lopettaa: "))

#Niksi: muutetaan lista-rakenne joukko-rakenteeksi => Joukko-rakenne poistaa automaattisesti diblikaatit

luvut_joukko = set(luvut)
 #luvut lista muutetaan joukoksi (set)

 #tulostetaan käyttäjän antamat erilaiset luvut
print("kaikki antamasi eri arvot:")
print(luvut_joukko)

print("Eri luvut allekkain: ")
for alkio in luvut_joukko:
    print(alkio)

#XTRA: tulostetaan käyttäjän antamat erilaiset luvut suurimmasta pienimpään

uniikit_lista = list(luvut_joukko)

# Listan alkiot laskevaan järjestykseen (suurin ensim)

uniikit_lista.sort(reverse=True)

print("Antamasi luvut suurimmasta pieninpään, kukin arvo vain kerran: ")
for alkio in uniikit_lista:
    print(alkio)
    

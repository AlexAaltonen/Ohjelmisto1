'''
    Tee ohjelma, joka kysyy käyttöjältä lukuja kunnes käyttäjä antaa negatiivisen luvun.
    Luvut talletetaan listaan, viimeistä eli negatiivista ei kuitenkaan talleteta listaan.
    Järjestä luvut suuruusjäjestykseen, pienin ensin.
    Tulosta sen jälkeen listan kaikki luvut.
    Tarkista sen jälkeen python koodilla, että onko luku 10 mukana listassa.
    Jos luku 10 on mukana, niin tulosta "luku 10 löytyi", muuten "lukua 10 ei löytynyt".
'''
#Luodaan uusi tyhjä lista käyttäjän antamia lukuja varaten

#kysytään käyttäjältä lukuja ja talletetaan ne listaan.
#lukujen kysysminen lopetataan kunnes saadaan negatiivinen luku.
#Negatiivista lukua ei talleteta listaan.

luvut = []

arvo = int(input("Anna kokonaisluku, negatiivinen arvo lopettaa: "))

while arvo >= 0:
    luvut.append(arvo)
    arvo = int(input("Anna kokonaisluku, negatiivinen arvo lopettaa: "))

luvut.sort()

print(luvut)

# onko arvo 10 listassa?
#Huom: nyt käytän boolean tyyppistä muuttujaa (saa arvon True tai false)

'''
loytyi = 10 in luvut
if loytyi == True:
    print("Arvo 10 löytyi")
else:
    print("Arvoa 10 EI löytynyt")
'''
loytyi = 10 in luvut

if loytyi:
    print("Arvo 10 löytyi")
else:
    print("Arvoa 10 EI löytynyt")

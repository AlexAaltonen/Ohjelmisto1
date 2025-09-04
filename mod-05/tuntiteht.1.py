loppuarvo = int(input("Anna kokonaisluku: "))

if loppuarvo <= 0:
    print("Antamasi luku ei kelppaa")
else:
    for luku in range(0, loppuarvo+1, 2):
        print(luku)


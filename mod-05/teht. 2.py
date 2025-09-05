luku = input("Anna lukuja, Enter lopettaa: ")

luvut = []



while luku != "":
    luvut.append(luku)
    luku = input("Anna lukuja, Enter lopettaa: ")
else:

    luvut.sort(reverse=True)
    print(luvut[0 : 6])
    print("ohjelma lopetettu")







vuosi = int(input("kirjoita vuosi luku: "))

if vuosi % 4 != 0:
    print("vuosi ei ole karkausvuosi")

elif vuosi % 100 == 0 and vuosi % 400 != 0:
    print("vuosi ei ole karkausvuosi")

else:
    print("vuosi on karkausvuosi")


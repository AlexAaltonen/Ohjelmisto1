vuoden_ajat = ("kevät", "kesä", "syksy", "talvi")

numero = int(input("Anna kuukauden numero: "))

if numero in range(4):
    print(vuoden_ajat[0])

elif numero in range(4, 7):
    print(vuoden_ajat[1])

elif numero in range (7, 10):
    print(vuoden_ajat[2])

elif numero in range(10, 13):
    print(vuoden_ajat[3])

else:
    print("Virheellinen kuukauden numero")



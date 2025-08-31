# N = pisteiden kokonaismäärä
# n = ympyrän siisään jääneiden pisteiden kokonaismäärä

#piste jää ympyrän sisaan vain jos se totteuttaa epäyhtälön x^2+y^2<1

# pi = 4n/N
import random

N = int(input("kirjoita testattavien pisteiden kokonaismäärä: "))

kerrat = 0
n = 0
while kerrat < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    kerrat = kerrat +1
    if x**2+y**2<1:
        n+=1

pi_likiarvo = 4 * n / N

print(f"piin likiarvo arvottujen pisteiden perusteella on: {pi_likiarvo}")


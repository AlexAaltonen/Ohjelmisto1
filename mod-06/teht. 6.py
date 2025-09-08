#cm^2 = 0.0001 m^2

import math

def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pizza_ala = math.pi *(sade**2) / 10000
    return hinta / pizza_ala

halkaisija1 = float(input("Anna pizza 1 halkaisija: "))
hinta1 = float(input("Anna pizza 1 hinta: "))

halkaisija2 = float(input("Anna pizza 2 halkaisija: "))
hinta2 = float(input("Anna pizza 2 hinta: "))

pizza1 = yksikkohinta(halkaisija1, hinta1)
pizza2 = yksikkohinta(halkaisija2, hinta2)

if pizza1 < pizza2:
    print("Pizza 1 on edullisempi")
elif pizza1 > pizza2:
    print("Pizza 2 on edullisempi")
else:
    print("Molemmat ovat yhtä halpoja")


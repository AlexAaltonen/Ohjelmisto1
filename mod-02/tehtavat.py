import math

kayttaja = input("Kirjoita nimesi: ")
print("Terve, " + kayttaja +"!")


ympyra_sade = input("Syötä ympyrän säde: ")

ympyra_ala = float(ympyra_sade) * math.pi ** 2

print(f"Ympyrän pinta-ala on: {ympyra_ala:.2f}")



suorakulmio_kanta_str = input("Syötä suorakulmion kanta: ")
suorakulmio_korkeus_str = input("Syötä suorakulmion korkeus: ")

suorakulmio_kanta = float(suorakulmio_kanta_str)
suorakulmio_korkeus = float(suorakulmio_korkeus_str)

suorakulmio_ala = suorakulmio_kanta * suorakulmio_korkeus
suorakulmio_piiri = 2 * suorakulmio_kanta + 2 * suorakulmio_korkeus

print(f"Suorakulmion pinta-ala on: {suorakulmio_ala:.2f}")
print(f"Suorakulmion piiri on: {suorakulmio_piiri:.2f}")

luku1_str = input("kirjoita numero 1: ")
luku2_str = input("kirjoita numero 2: ")
luku3_str = input("kirjoita numero 3: ")

luku1 = float(luku1_str)
luku2 = float(luku2_str)
luku3 = float(luku3_str)

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

print(f"Numeroiden summa on: {summa}")
print(f"Numeroiden tulo on: {tulo}")
print(f"Numertoiden keskiarvo on: {keskiarvo}")

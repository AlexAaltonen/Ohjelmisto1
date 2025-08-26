luku1_str = input("kijoita numero 1: ")
luku2_str = input("kirjoita numero 2: ")
luku3_str = input("kirjoita numero 3: ")

luku1 = float(luku1_str)
luku2 = float(luku2_str)
luku3 = float(luku3_str)

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3

print(f"Lukujen summa on: {summa:.2f}")
print(f"Lukujen tulo on: {tulo:.2f}")
print(f"Lukujen keskiarvo on: {keskiarvo:.2f}")

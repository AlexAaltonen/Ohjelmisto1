import math

ympyra_sade_str = input("kirjoita ympyrän säde: ")
ympyra_sade = float(ympyra_sade_str)

ympyra_pinta_ala = math.pi * ympyra_sade ** 2

print(f"Ympyrän pinta-ala on: {ympyra_pinta_ala:.2f}")

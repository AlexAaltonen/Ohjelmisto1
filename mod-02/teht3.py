suorakulmio_kanta_str = input("kirjoita suorakulmion kanta: ")
suorakulmio_korkeus_str = input("kirjoita suorakulmion korkeus: ")

suorakulmio_kanta = float(suorakulmio_kanta_str)
suorakulmio_korkeus = float(suorakulmio_korkeus_str)

suorakulmio_pinta_ala = suorakulmio_kanta * suorakulmio_korkeus
suorakulmio_piiri = 2 * suorakulmio_kanta + 2 * suorakulmio_korkeus

print(f"suorakulmion pinta-ala on: {suorakulmio_pinta_ala:.2f}")
print(f"suorakulmion piiri on: {suorakulmio_piiri:.2f}")

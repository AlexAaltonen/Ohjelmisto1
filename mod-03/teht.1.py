
kuha_pituus = float(input("Anna kuhan pituus: "))
alin_sallittu = 37 - kuha_pituus
if kuha_pituus <= 36:
    print("Laske kuha takaisin järveen")
    print(f"{alin_sallittu} senttiä liian lyhyt")

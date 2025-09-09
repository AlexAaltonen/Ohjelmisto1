def parillinen(lista):
    parillinen_lista = []
    for luku in lista:
        if luku % 2 == 0:
            parillinen_lista.append(luku)
    return parillinen_lista



alkuperainen_lista=[1, 2, 3 ,4, 5, 6]

parillinen_lista = parillinen(alkuperainen_lista)

print(parillinen_lista)

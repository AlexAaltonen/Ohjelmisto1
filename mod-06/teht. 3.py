
def muutos(x):
    return x * 3.785


while True:
    maara = float(input("Anna gallonien määrä: "))
    if maara < 0:
        print("Ei saa olla negatiivinen arvo")
        break
    litra = muutos(maara)
    print(f"{litra:.2f} litraa")









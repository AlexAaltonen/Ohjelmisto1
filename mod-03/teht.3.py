sukupuoli = input("Kirjoita biologinen sukupuolesi: ")

if sukupuoli == "Mies":
    hemoglobiini= float(input("Kerro hemoglobiini arvosi: "))
    if hemoglobiini <= 134:
        print("Hemoblobiinisi on alhainen")
    if 134 <= hemoglobiini <= 195:
        print("Hemoglobiinisi on normaali")
    if  hemoglobiini >= 195:
        print("Hemoglobiinisi on korkea")


if sukupuoli == "Nainen":
    hemoglobiini= float(input("kerro hemoglobiini arvosi: "))
    if hemoglobiini <= 117:
        print("Hemoblobiinisi on alhainen")
    if 117 <= hemoglobiini <= 175:
        print("Hemoglobiinisi on normaali")
    if  hemoglobiini >= 175:
        print("Hemoglobiinisi on korkea")
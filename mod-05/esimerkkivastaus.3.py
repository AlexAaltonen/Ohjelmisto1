num = int(input("Anna kokonaisluku: "))

if num < 2:
    print(f"{num} ei ole alkuluku")
else:
    isPrime = True
    for i in range(2, num):
    #for i in range(2, int(num**0.5) + 1):
    #jos jakolasku menee tasan -> ei ole alkuluku -> lopetetaan
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
    #if isPrime == True: # ylempi merkintä lyhennys tästä
        print(f"{num} on alkuluku")
    else:
        print(f"{num} ei ole alkuluku")


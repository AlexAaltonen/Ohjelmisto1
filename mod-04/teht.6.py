# A = yksikkö ympyrä, jonka keskipiste origossa ja säde on yksi

# B = A:n ympäri piirretty neliö
    # nurkka pisteet ovat (-1,-1), (1,-1), (1,1), (-1,1)
#ympyrän pinta-ala neliön pinta-alasta on pi/4

# N = pisteiden kokonaismäärä
# n = ympyrän siisään jääneiden pisteiden kokonaismäärä
# n/n on noin pi/4

#piste toimii vain jos se totteuttaa epäyhtälön x^2+y^2<1

# N
import random
pisteiden_kokonaismaara = int(input("kirjoita testattavien pisteiden kokonaismäärä: "))

kerrat = 0

while kerrat < pisteiden_kokonaismaara:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    kerrat = kerrat +1
    print(x,y)


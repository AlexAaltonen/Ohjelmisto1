cities=[]

for i in range(5):
    city = input(f"Anna kaupungin nimi {i+1}/5: ")
    cities.append(city)

print("Syötetyt kaupungit:")
for city in cities:
    print(city)


import mysql.connector
from geopy import distance

#Muistiinpanot
#fetchall ei toimi vaikka se antaa vain yhden arvon sillä se luo listan
#geopy distance vaatii tupleja eikä listoja


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='Alex',
         password='MasaRektaa69',
         autocommit=True
         )

icao_koodi1 = input("Anna lentokentän icao-koodi: ")
sql=f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
kursori = yhteys.cursor()
kursori.execute(sql, (icao_koodi1,))
rivi1 = kursori.fetchone()
print(rivi1)



icao_koodi2 = input("Anna toisen lentokentän icao-koodi: ")
sql=f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
kursori = yhteys.cursor()
kursori.execute(sql, (icao_koodi2,))
rivi2 = kursori.fetchone()
print(rivi2)

matka = distance.distance(rivi1,rivi2).km

print(f"Lentokenttien etäisyys on: {matka:.2f}km")


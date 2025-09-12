import mysql.connector

def hae_tyypit(maakoodi):
    sql = f"SELECT type, count(type) FROM airport where iso_country = %s Group by type"
    kursori = yhteys.cursor()
    kursori.execute(sql, (maakoodi,))
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            print(f"Tyyppi: {rivi[0]}")
            print(f"niiden lukumäärä: {rivi[1]}")



    else:
        print("kenttää ei löytynyt")
    kursori.close()
    yhteys.close()
    return


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='Alex',
         password='MasaRektaa69',
         autocommit=True
         )

maakoodi = input("Kirjoita maakoodi: ")
hae_tyypit(maakoodi)
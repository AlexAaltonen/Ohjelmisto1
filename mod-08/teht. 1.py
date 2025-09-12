from fileinput import close

import mysql.connector


#jos ident = %s niin sulkuihin (jotai,) esim kursori.execute(sql, (icao_koodi,)) toimii

#jos idnet = {icao_koodi} niin pelkkä kursori.execute(sql) toimii

def hae_icao_koodit(icao_koodi):
    sql = f"SELECT name, municipality FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao_koodi,))
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            print(f"Lentokenttä: {rivi[0]}")
            print(f"Sijaitsee: {rivi[1]}")
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

icao_koodi = input("kirjoita lentoaseman ICAO-koodi: ")
hae_icao_koodit(icao_koodi)














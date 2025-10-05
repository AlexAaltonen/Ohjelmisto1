import mysql.connector


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='Alex',
         password='MasaRektaa69',
         autocommit=True
         )

def haelentokentat():
    sql ="SELECT * FROM airport"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def haelentokentta(koodi):
    sql= f"SELECT * FROM airport WHERE ident=%s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (koodi,))
    tulos = kursori.fetchone()
    return tulos


code=input('syötäkoodi:')
kentta = haelentokentta(code)
print(kentta['name'], kentta["kentta"])

#print(haelentokentta("EFHK"))

#kentat = haelentokentat()

#for kentta in kentat:
    #print(f"nimi: {kentta['name']}")


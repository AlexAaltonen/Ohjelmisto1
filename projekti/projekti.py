import mysql.connector
import random
'''
pelaaja tarvitsee pisteet, nimen, random lokaation, ja oman id

valitaan ensin chosen_airports taulusta yksi randomi lentokentttä, josta pelaaja aloittaa pelin

jonka jälkeen lisätään pelaaja tauluun player arvot name, points, location

haetaan pelaajan id ja palautetaan se --> tarvitaan muualla esim. onko käyttäjältä kysytty jo tämä kysysmys
haetaan sijainti ja palautetaan se
'''
conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='Alex',
        password='MasaRektaa69',
        autocommit=True
)



def add_player(name, starting_points=1000):
    cursor = conn.cursor()
    cursor.execute("select ident from chosen_airports")
    airports = cursor.fetchall()
    starting_location = random.choice(airports)[0]

    sql = "insert into player (name, points, location) VALUES(%s, %s, %s)"
    cursor.execute(sql, (name, starting_points, starting_location))
    conn.commit()

    player_id = cursor.lastrowid
    print(f"Pelaajan nimi: {name}, ID: {player_id}, lokaatio on: {starting_location}")

    cursor.close()
    conn.close()

    return player_id, starting_location




'''
projekti valitse random lentokentät 
'''

def game_airports():
    cursor = conn.cursor()
    cursor.execute("select distinct continent from airport where continent is not null")
    continents = [row[0] for row in cursor.fetchall()]
    print(continents)


    chosen_continent = random.choice(continents)
    print(f"Valittu maanosa: {chosen_continent}")


    cursor.execute('''
    select ident
    from airport
    where continent = %s
    limit 30
    ''',(chosen_continent,))

    chosen_airports = [row[0] for row in cursor.fetchall()]
    print(f"valitut lentokentät ovat: {chosen_airports}")

    special_ident = random.choice(chosen_airports)

    for ident in chosen_airports:
        special = 1 if ident == special_ident else 0
        cursor.execute('''
        insert into chosen_airports (ident, special, visited)
        values(%s, %s, 0)
        ''',(ident, special))

    conn.commit()


game_airports()


def calculate_prize():
    cursor = conn.cursor()

    player= get_player()
    player_id = player['ID']
    sql = '''select task.points
    from chosen_tasks
    join task on chosen_tasks.task_id = task.id
    join task_choices on task.id = task_choices.task_id
    join answer on task_choices.answer_id = answer.id
    where chosen_tasks.player_id = %s
    and chosen_tasks.answered = 1
    and answer.is_correct = 1
    '''

    cursor.execute(sql, (player_id,))
    result = cursor.fetchall()

    print(player_id)
    print(result)



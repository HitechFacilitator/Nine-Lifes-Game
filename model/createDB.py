
import os
import sqlite3

DB = os.path.join(os.path.dirname(__file__), "NLG")

game_query = "CREATE TABLE Game (" \
             "id_game int AUTO_INCREMENT PRIMARY KEY," \
             " nb_of_players int, " \
             "date timestamp," \
             ");"
player_query = "CREATE TABLE Player (" \
               "id_player varchar(20) PRIMARY KEY, " \
               "player_name varchar(30)," \
               "email varchar(30)," \
               "rank int," \
               "nb_game_played int," \
               "nb_game_loosed int," \
               "nb_game_won int" \
               ");"
category_query = "CREATE TABLE Category (" \
                 "id_category AUTO_INCREMENT PRIMARY KEY," \
                 "category_name varchar(20)," \
                 "nb_of_questions int" \
                 ");"
playerGame_query = "CREATE TABLE PlayGame(" \
                   "id_playerGame int AUTO_INCREMENT PRIMARY KEY," \
                   "id_player varchar(20)," \
                   "id_game int" \
                   "FOREIGN KEY (id_player) REFERENCES (Player)" \
                   "FOREIGN KEY (id_game) REFERENCES (Game)" \
                   ");"

with sqlite3.connect(DB) as connection:
    cursor = connection.cursor()
    for query in [game_query, player_query, category_query, playerGame_query]:
        cursor.execute(query)

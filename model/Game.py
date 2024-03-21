import sqlite3

from base_model import AbstractBaseModel


class Game(AbstractBaseModel):
    def __init__(self, id_game, nb_of_players, date):
        self.id_game = id_game,
        self.nb_players = nb_of_players,
        self.date = date

    def create(self):
        query = "INSERT INTO Game (nb_of_players, date) VALUES (?,?);"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query, (self.nb_players, self.date))

    def read(self):
        query = "SELECT * FROM Game;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            results = cursor.execute(query).fetchall()
            display = []
        for result in results:
            game = Game(id_game=result[0], nb_of_players=result[1], date=result[2])
            display.append(game)

        return display

    def readbyid(self, i):
        query = "SELECT * FROM Game WHERE id_game=?;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            result = cursor.execute(query, i).fetchone()

        return result

    def update(self, i):
        query = "UPDATE Game SET nb_of_players=?, date=? WHERE id_game=?;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query, (self.nb_players, self.date, self.id_game))

    def deletebyid(self, i):
        query = "DELETE FROM Game WHERE id_game=?;;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query, i)

    def delete(self):
        query = "DELETE FROM Game;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query)

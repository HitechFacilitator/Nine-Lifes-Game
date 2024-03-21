import sqlite3

from base_model import AbstractBaseModel


class Game(AbstractBaseModel):
    def __init__(self, nb_of_players=None, date=None):
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
            game = Game(nb_of_players=result[1], date=result[2])
            display.append(game)

        return display

    def readById(self, i=None):
        query = "SELECT * FROM Game WHERE date=?;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            result = cursor.execute(query, self.date).fetchone()

        return result

    def update(self, i=None):
        if i is not None:
            query = "UPDATE Game SET nb_of_players=?, date=? WHERE id_game=?;"
            with sqlite3.connect("NLG") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.nb_players, self.date, i))
            return
        return "No Id for the update"

    def deleteById(self, i=None):
        query = "DELETE FROM Game WHERE date=?;;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query, self.date)

    def delete(self):
        query = "DELETE FROM Game;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query)

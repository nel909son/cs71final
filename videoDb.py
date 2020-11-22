from tkinter import *

from PIL import ImageTk,Image

import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Movie_Master(id INTEGER PRIMARY KEY,
                                                                    movieID integer,
                                                                    movieName text,
                                                                    movieGenre text,
                                                                    movieYear integer)''')
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM Movie_Master")
        rows = self.cur.fetchall()
        return rows

    def insert(self, movieID,movieName,movieGenre,movieYear):
        self.cur.execute("INSERT INTO Movie_Master VALUES (NULL,?,?,?,?)",(movieID, movieName,movieGenre,movieYear))
        self.conn.commit()

    def remove(self, movieID):
        self.cur.execute("DELETE FROM Movie_Master WHERE movieID=?",(movieID,))
        self.conn.commit()

    def update(self, movieId, movieName, movieGenre, movieYear):
        self.cur.execute("UPDATE Movie_Master SET movieName=?, movieGenre=?, movieYear=? WHERE movieID", (movieName,movieGenre,movieYear,movieID))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

path = "C:/Users/nelso/Desktop/python/71final/"

db = Database(path+'Movie.db')

#db.insert(111,"mother!","reality",2018)

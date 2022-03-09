import random as r
from uuid import uuid4
import sqlite3

db = sqlite3.connect('codes.sqlite3')
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS codes(
    ids TEXT NOT NULL,
    code INT NOT NULL
)""")
db.commit()


class Generate:
    def __init__(self):

        ids = str(uuid4())
        code = (r.randint(1000,9999))

        cursor.execute("INSERT INTO codes VALUES(?, ?)", (ids, code))
        db.commit()

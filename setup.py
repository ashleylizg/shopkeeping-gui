import sqlite3
from contextlib import closing

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE items (name TEXT, quantity INTEGER, price INTEGER)")
connection.commit()
connection.close()
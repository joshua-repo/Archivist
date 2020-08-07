import sqlite3

conn = sqlite3.connect(r"../backups/Archives.db")
cur = conn.cursor()
cur.execute("")
#print("Initialize Library successfully")
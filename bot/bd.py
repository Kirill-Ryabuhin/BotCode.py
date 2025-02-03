import sqlite3

with sqlite3.connect('heroes.db') as db:
    cur = db.cursor()
    query = """CRATE TABLE IF NOT EXISTS heroes(name TEXT, weight INTEGER"""
    query1 = """INSERT INTO heroes (name, weight) VALUES (Lifestiller, 6) """
    query1 = """INSERT INTO heroes (name, weight) VALUES (Lifestiller, 6) """
    query1 = """INSERT INTO heroes (name, weight) VALUES (Lifestiller, 6) """
    query1 = """INSERT INTO heroes (name, weight) VALUES (Lifestiller, 6) """
    query1 = """INSERT INTO heroes (name, weight) VALUES (Lifestiller, 6) """
    cur.execute(query)
    pass




db.close()

#ser el main con el usuario para la manipulacion de la base de datos
import sqlite3

if __name__ == '__main__':
	con = sqlite3.connect(r"unzip/LOTUS_2021_03_simple.sdf")
	cur = con.cursor()
	cur.execute("CREATE TABLE movie(title, year, score)")


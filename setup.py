import sqlite3
from courses import courses
from random import randint
import random
import rich

print("Welcome to the Simple Golf Tracking App")
print("")
print("This app was built on streamlit in python mainly for use by players of Walkabout Mini-Golf, but can be used to track real life golf games as well")
print("")
print("After this window closes run 'launch.bat' to run the app \n")

WMCInstall = str(input("Press Enter To Run Setup"))



conn = sqlite3.connect("golfstats.db")
cur = conn.cursor()
cur.execute(f"""CREATE TABLE courses(name, easy, hard)""")
conn.commit()


for course in courses:
    cur.execute("""INSERT INTO courses(name, easy, hard) VALUES (?, ?, ?)""", (course["name"], course["easy_par"], course["hard_par"]))
    conn.commit()

cur.execute("""CREATE TABLE games (course, difficulty, hole_1, hole_2,hole_3,hole_4,hole_5,hole_6,hole_7,hole_8,hole_9,hole_10,hole_11,
            hole_12,hole_13,hole_14,hole_15,hole_16,hole_17,hole_18, total_score, putter, date)""")

conn.commit()


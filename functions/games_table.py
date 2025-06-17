import pandas as pd
import sqlite3
import pandas as pd

def load_table(course: str, difficulty: str) -> pd.DataFrame | None:
    conn = sqlite3.Connection("golfstats2.db")
    df = pd.read_sql_query("SELECT * FROM games WHERE course_name = :course AND difficulty = :difficulty", conn, params={"course": course, "difficulty": difficulty})

    df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date
    df["time"] = pd.to_datetime(df["time"], format="%H:%M", errors="coerce").dt.time

    return df

def load_table_hole(course: str, difficulty: str, hole: int) -> pd.DataFrame | None:
    conn = sqlite3.Connection("golfstats2.db")
    df = pd.read_sql_query(f"""SELECT course_name, difficulty, date, time, putter, hole_{hole} 
                           FROM games WHERE course_name = :course AND difficulty = :difficulty""", 
                           conn, params={"course": course, "difficulty": difficulty})

    df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date
    df["time"] = pd.to_datetime(df["time"], format="%H:%M", errors="coerce").dt.time

    return df







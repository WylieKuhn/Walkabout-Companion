import sqlite3
import pandas as pd

def load_games_dataframe(database: str):
    conn = sqlite3.connect(database)

    query = "SELECT * FROM games"
    df = pd.read_sql_query(query, conn)
    df["date"] = pd.to_datetime(df["date"], format = "%Y-%m-%d").dt.date
    df["time"] = pd.to_datetime(df["time"], format="%H:%M:%S").dt.time

    conn.close()

    if len(df) <= 0:
        return None
    else:
        return df

def load_courses_dataframe(database: str):
    conn = sqlite3.connect(database)

    query = "SELECT * FROM courses"
    df = pd.read_sql_query(query, conn)
    

    conn.close()

    if len(df) <= 0:
        return None
    else:
        return df



import pandas as pd
import sqlite3

def load_table(course: str, difficulty: str) -> pd.DataFrame:
    conn = sqlite3.connect("golfstats.db")

    query = """SELECT * FROM games WHERE name = ? AND difficulty = ?"""

    df = pd.read_sql_query(query, conn, params=(course, difficulty))

    conn.close()
    
    if len(df) <= 0:
        return None
        
    else:
        
        df["date"] = pd.to_datetime(df["date"], format = "%Y-%m-%d")

        return df


import polars as pl
import sqlite3

def load_table(course: str, difficulty: str) -> pl.DataFrame:
    conn = sqlite3.connect("golfstats.db")
    cursor = conn.cursor()

    query = """SELECT * FROM games WHERE course = ? AND difficulty = ?"""

    cursor.execute(query, (course,difficulty,))
    rows = cursor.fetchall()

    column_names = [description[0] for description in cursor.description]

    df = pl.DataFrame(rows, schema=column_names)

    conn.close()

    df = df.with_columns(
        pl.col("date").str.strptime(pl.Date, "%Y-%m-%d")
    )

    return df


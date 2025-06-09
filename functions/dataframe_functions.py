import sqlite3
import pandas as pd

def load_dataframe(database: str)
    conn = sqlite3.connect(database)

    query = "SELECT * FROM employees"
    df = pd.read_sql_query(query, conn)

    print(df)

    conn.close()

    return df

def convert_date_to_object(dataframe):
    dataframe 
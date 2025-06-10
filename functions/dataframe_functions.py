import sqlite3
import pandas as pd

def load_dataframe(database: str):
    conn = sqlite3.connect(database)

    query = "SELECT * FROM employees"
    df = pd.read_sql_query(query, conn)

    conn.close()

    return df

def convert_date_to_object(dataframe: pd.DataFrame):
    converted_dataframe = dataframe
    print(converted_dataframe)
    converted_dataframe["date"] = pd.to_datetime(converted_dataframe['date'], format='%Y-%m-%d')
    
    return converted_dataframe

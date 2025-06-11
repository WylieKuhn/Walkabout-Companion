import pandas as pd
import sqlite3
from functions.dataframe_functions import load_courses_dataframe, load_games_dataframe

def percent_easy_under_par():
    db = "golfstats.db"
    games_df = load_games_dataframe(db)
    courses_df = load_courses_dataframe(db)

    merged_df = pd.merge(games_df, courses_df, on="name")

    easy_df = merged_df[merged_df["difficulty"].str.lower() == "easy"]

    easy_df["over_under"] = easy_df["total_score"] - easy_df["easy"]

    num_under_par = (easy_df["over_under"] < 0).sum()
    total_games = len(easy_df)

    if total_games == 0:
        return 0.0  

    percent = (num_under_par / total_games) * 100
    return round(percent, 2)

def percent_hard_under_par():
    db = "golfstats.db"
    games_df = load_games_dataframe(db)
    courses_df = load_courses_dataframe(db)

    merged_df = pd.merge(games_df, courses_df, on="name")

    easy_df = merged_df[merged_df["difficulty"].str.lower() == "hard"]

    easy_df["over_under"] = easy_df["total_score"] - easy_df["hard"]

    num_under_par = (easy_df["over_under"] < 0).sum()
    total_games = len(easy_df)

    
    if total_games == 0:
        return 0.0  

    percent = (num_under_par / total_games) * 100
    return round(percent, 2)


def percent_under_par_course(course: str, difficulty: str):
    db = "golfstats.db"
    conn = sqlite3.connect(db)

    query = "SELECT * FROM games WHERE name = ? AND difficulty = ?"
    games_df = pd.read_sql_query(query, conn, params=(course, difficulty))

    courses_df = load_courses_dataframe(db)

    merged_df = pd.merge(games_df, courses_df, on="name")

    difficulty = difficulty.lower()
    if difficulty == "easy":
        par_column = "easy"
    elif difficulty == "hard":
        par_column = "hard"
    else:
        raise ValueError("Difficulty must be 'Easy' or 'Hard'")

    merged_df["over_under"] = merged_df["total_score"] - merged_df[par_column]

    num_under_par = (merged_df["over_under"] < 0).sum()
    total_games = len(merged_df)

    if total_games == 0:
        return "0.0%"

    percent = (num_under_par / total_games) * 100
    return f"{round(percent, 2)}%"


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
    db = "golfstats2.db"
    conn = sqlite3.connect(db)

    games_query = "SELECT * FROM games WHERE course_name = ? AND difficulty = ?"
    games_df = pd.read_sql_query(games_query, conn, params=(course, difficulty))

    courses_query = "SELECT * FROM courses WHERE course_name = ? AND difficulty = ?"
    courses_df = pd.read_sql_query(courses_query, conn, params=(course, difficulty))

    conn.close()

    if games_df.empty or courses_df.empty:
        return "0.0%"
    
    merged_df = pd.merge(games_df, courses_df, on=["course_name", "difficulty"])
    if merged_df.empty:
        return "0.0%"

    merged_df["over_under"] = merged_df["total_score"] - merged_df["total_par"]
    print(merged_df[["total_score", "total_par", "over_under"]])

    num_under_par = (merged_df["over_under"] < 0).sum()
    total_games = len(merged_df)

    if total_games == 0:
        return "0.0%"

    percent = (num_under_par / total_games) * 100
    return f"{round(percent, 2)}%"

def percent_under_par_hole(course: str, difficulty: str, hole: int) -> str:
    db = "golfstats2.db"
    conn = sqlite3.connect(db)

    hole_score_col = f"hole_{hole}"
    hole_par_col = f"hole_{hole}_par"

    par_query = f"""
        SELECT {hole_par_col} FROM courses
        WHERE course_name = ? AND difficulty = ?
    """
    par_result = conn.execute(par_query, (course, difficulty)).fetchone()
    if not par_result or par_result[0] is None:
        return "0.0%"  

    par_value = par_result[0]

    game_query = f"""
        SELECT {hole_score_col} FROM games
        WHERE course_name = ? AND difficulty = ?
    """
    scores_df = pd.read_sql_query(game_query, conn, params=(course, difficulty))
    scores_df = scores_df.dropna()

    if scores_df.empty:
        return "0.0%"  

    num_under_par = (scores_df[hole_score_col] < par_value).sum()
    total = len(scores_df)

    percent = (num_under_par / total) * 100
    return f"{round(percent, 2)}%"


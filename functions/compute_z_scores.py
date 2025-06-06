import statistics
import sqlite3

def compute_z_scores(course: str, difficulty:str) -> list:
    """
    Takes in the course name and returns a list of z-scores of games played on
    the selected course for use in statistical analysis and display.

    Args: course: str

    Returns: List
    """
    conn = sqlite3.connect("golfstats.db")
    cur = conn.cursor()

    total_scores = []
    z_scores = []
    data = cur.execute("""SELECT * FROM games
                        WHERE course = ? AND difficulty = ?""", (course,difficulty,))
    
    for total in data.fetchall():
        total_scores.append(total[20])
    
    if len(total_scores) > 1:
        for score in total_scores:
            zScore = round((score-statistics.mean(total_scores))/statistics.pstdev(total_scores),3)
            z_scores.append(zScore)

    
    return z_scores
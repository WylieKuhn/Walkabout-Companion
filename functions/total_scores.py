import sqlite3

def total_scores(course: str, difficulty: str) -> list:
    conn = sqlite3.connect("golfstats.db")
    cur = conn.cursor()

    data = cur.execute("""SELECT * FROM games
                        WHERE course = ? AND difficulty = ?""", (course, difficulty,))
    
    total_scores_list = []

    for total in data.fetchall():
        total_scores_list.append(total[20])

    return total_scores_list



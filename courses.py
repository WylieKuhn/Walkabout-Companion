import sqlite3

courses = [
    {"name": "Tourist Trap", "easy_par": 57, "hard_par": 61},
    {"name": "Cherry Blossom", "easy_par": 63, "hard_par": 67},
    {"name": "Seagull Stacks", "easy_par": 62, "hard_par": 67},
    {"name": "Arizona Modern", "easy_par": 66, "hard_par": 65},
    {"name": "Original Gothic", "easy_par": 54, "hard_par": 64},
    {"name": "Tethys Station", "easy_par": 63, "hard_par": 64},
    {"name": "Bogey's Bonanza", "easy_par": 60, "hard_par": 67},
    {"name": "Quixote Valley", "easy_par": 54, "hard_par": 60},
    {"name": "Sweetopia", "easy_par": 55, "hard_par": 59},
    {"name": "Upside Town", "easy_par": 58, "hard_par": 63},
    {"name": "Alfheim", "easy_par": 57, "hard_par": 61},
    {"name": "Widow's Walkabout", "easy_par": 61, "hard_par": 60},
    {"name": "Labyrinth", "easy_par": 64, "hard_par": 65},
    {"name": "Myst", "easy_par": 61, "hard_par": 63},
    {"name": "Meow Wolf", "easy_par": 57, "hard_par": 57},
    {"name": "Gardens of Babylon", "easy_par": 61, "hard_par": 64},
    {"name": "Shangri-La", "easy_par": 64, "hard_par": 68},
    {"name": "El Dorado", "easy_par": 62, "hard_par": 61},
    {"name": "Atlantis", "easy_par": 59, "hard_par": 59},
    {"name": "Temple of Zerzura", "easy_par": 63, "hard_par": 60},
    {"name": "20,000 Leagues Under the Sea", "easy_par": 59, "hard_par": 60},
    {"name": "Journey to the Center of the Earth", "easy_par": 56, "hard_par": 60},
    {"name": "Around the World in 80 Days", "easy_par": 57, "hard_par": 56},
    {"name": "Laser Lair", "easy_par": 57, "hard_par": 58},
    {"name": "Venice", "easy_par": 58, "hard_par": 60},
    {"name": "Ice Lair", "easy_par": 61, "hard_par": 59},
    {"name": "Mars Gardens", "easy_par": 58, "hard_par": 60},
    {"name": "Viva Las Elvis", "easy_par": 57, "hard_par": 60},
    {"name": "Wallace & Gromit", "easy_par": 55, "hard_par": 55},
    {"name": "Holiday Hideaway", "easy_par": 56, "hard_par": 55},
    {"name": "Mount Olympus", "easy_par": 61, "hard_par": 62},
    {"name": "Raptor Cliff's", "easy_par": 59, "hard_par": 59}

]


def get_courses():
    conn = sqlite3.connect("golfstats.db")
    cur = conn.cursor()
    course_names = cur.execute("""SELECT DISTINCT name FROM courses""")
    list_of_course_names = []
    
    for course in course_names.fetchall():
        list_of_course_names.append(course[0])
    return list_of_course_names



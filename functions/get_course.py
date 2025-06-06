import sqlite3

def get_courses() -> list:
    """ 
    Gets a list of all the course names and returns a list of them to pass
    to various streamlit elements.

    Args: None

    Returns: List

    """
    #Open database connection
    conn = sqlite3.connect("golfstats.db")
    cur = conn.cursor()

    #Get list of course names
    course_names = cur.execute("""SELECT DISTINCT name FROM courses""")

    #Initialize list of course names
    list_of_course_names = []
    
    #Add all course names to list
    for course_name in course_names.fetchall():
        list_of_course_names.append(course_name[0])

    #Sorts the list because I am too lazy to write the course names in alphabetical order as they come out.
    list_of_course_names.sort()

    #Returns the list
    return list_of_course_names
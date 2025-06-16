import sqlite3
import json
from sqlalchemy import create_engine, select, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from models.database_models import Course, Game, Base

Base = declarative_base()

def validate_course_pars(course_list):
    mismatches = []

    for course in course_list:
        hole_pars_sum = sum(course.get(f"hole_{i}_par", 0) for i in range(1, 19))
        if hole_pars_sum != course.get("total_par", 0):
            mismatches.append({
                "name": course.get("name"),
                "difficulty": course.get("difficulty"),
                "expected_total": hole_pars_sum,
                "reported_total": course.get("total_par")
            })
    if len(mismatches) > 0:
        return mismatches
    else:
        return "All courses have correct pars"

def get_courses():
    conn = sqlite3.connect("golfstats.db")
    cur = conn.cursor()
    course_names = cur.execute("""SELECT DISTINCT name FROM courses""")
    list_of_course_names = []
    
    for course in course_names.fetchall():
        list_of_course_names.append(course[0])

    list_of_course_names.sort()
    
    return list_of_course_names

def get_courses_putter():
    conn = sqlite3.connect("golfstats.db")
    cur = conn.cursor()
    course_names = cur.execute("""SELECT DISTINCT name FROM courses""")
    list_of_course_names = []
    
    for course in course_names.fetchall():
        list_of_course_names.append(course[0])

    list_of_course_names.append("Standard")
    list_of_course_names.sort()

    return list_of_course_names

def get_course_names():
    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import sessionmaker
      # Replace with the actual module name

    # Connect to the database
    engine = create_engine("sqlite:///golfstats2.db", echo=False)
    SessionLocal = sessionmaker(bind=engine)

    # Create session
    session = SessionLocal()

    # Query unique course names
    unique_course_names = session.query(Course.course_name).distinct().all()

    # Flatten to a simple list of strings
    course_list = [name[0] for name in unique_course_names]

    # Optional: print the list
    # Close session
    session.close()
    return course_list





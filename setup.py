from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.database_models import Course, Game, Base  # <-- Import, don't redefine
import json

print("Welcome to the Simple Golf Tracking App")
print("")
print("This app was built on streamlit in python mainly for use by players of Walkabout Mini-Golf, but can be used to track real life golf games as well")
print("")
print("After this window closes run 'launch.bat' to run the app \n")

WMCInstall = str(input("Press Enter To Run Setup"))

DATABASE_FILE = "golfstats2.db"
engine = create_engine(f"sqlite:///{DATABASE_FILE}", echo=False)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


with open("functions/courses.json", "r") as file:
    courses_data = json.load(file)

try:
    with Session() as session:
        for course_dict in courses_data:
            # Rename 'name' to 'course_name' to match the model
            course_dict["course_name"] = course_dict.pop("name")

            course = Course(**course_dict)
            session.add(course)
        session.commit()
except Exception as e:
    print("Error creating courses:", e)
    session.rollback()

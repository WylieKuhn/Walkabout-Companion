import random
from datetime import datetime
from functions.courses import get_course_names
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from models.database_models import Course, Game, Base


fake = Faker()

difficulties = ["easy", "hard"]
def generate_fake_game():
    course = random.choice(get_course_names())
    difficulty = random.choice(difficulties)
    player_id = 1
    date = fake.date_between(start_date='-2y', end_date='today').isoformat()
    time = fake.time(pattern="%H:%M")
    putter = "Venice"

    hole_scores = [random.randint(1, 6) for _ in range(18)]
    total_score = sum(hole_scores)
    game = Game(
        course_name=course,
        difficulty=difficulty,
        player_id=player_id,
        date=date,
        time=time,
        total_score=total_score,
        putter=putter,
        hole_1=hole_scores[0],
        hole_2=hole_scores[1],
        hole_3=hole_scores[2],
        hole_4=hole_scores[3],
        hole_5=hole_scores[4],
        hole_6=hole_scores[5],
        hole_7=hole_scores[6],
        hole_8=hole_scores[7],
        hole_9=hole_scores[8],
        hole_10=hole_scores[9],
        hole_11=hole_scores[10],
        hole_12=hole_scores[11],
        hole_13=hole_scores[12],
        hole_14=hole_scores[13],
        hole_15=hole_scores[14],
        hole_16=hole_scores[15],
        hole_17=hole_scores[16],
        hole_18=hole_scores[17],
    )

    return game

def populate_fake_games(n=10000):
    engine = create_engine("sqlite:///golfstats2.db", echo=False)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    try:
        for game in range(n):
            fake_game = generate_fake_game()
            session.add(fake_game)
            print(f"Added fake game {game + 1} of {n}.")
            session.commit()
        print(f"Inserted {n} fake games.")
    except Exception as e:
        session.rollback()
        print("Error inserting games:", e)
    finally:
        session.close()

populate_fake_games(10000)


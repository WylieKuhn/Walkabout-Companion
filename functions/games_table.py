import pandas as pd
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from models.database_models import Game

def load_table(course: str, difficulty: str) -> pd.DataFrame | None:
    engine = create_engine("sqlite:///golfstats2.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    query = select(Game).where(
        Game.course_name == course,
        Game.difficulty == difficulty
    )
    print(query)


    with engine.connect() as conn:
        df = pd.read_sql(query, conn, params={"course": course, "difficulty": difficulty})
        print(df)

    if df.empty:
        return None
    else:
        df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
        return df




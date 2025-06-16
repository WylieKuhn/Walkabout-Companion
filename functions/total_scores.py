from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.database_models import Game  # or Games

def total_scores(course: str, difficulty: str) -> list:
    engine = create_engine("sqlite:///golfstats2.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query total_score for matching games
        results = (
            session.query(Game.total_score)
            .filter(Game.course_name == course, Game.difficulty == difficulty)
            .all()
        )

        # Extract values from result tuples
        total_scores_list = [row[0] for row in results]
        session.close()
        return total_scores_list

    finally:
        session.close()



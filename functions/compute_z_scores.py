from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.database_models import Game  # or Games, adjust as needed
import statistics

def compute_z_scores(course: str, difficulty: str) -> list:
    engine = create_engine("sqlite:///golfstats2.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query only total_score values
        scores = (
            session.query(Game.total_score)
            .filter(Game.course_name == course, Game.difficulty == difficulty)
            .all()
        )

        # Extract just the values from the SQLAlchemy result
        total_scores = [score[0] for score in scores]

        if len(total_scores) <= 1:
            return []

        # Compute Z-scores
        mean = statistics.mean(total_scores)
        stdev = statistics.pstdev(total_scores)
        z_scores = [round((score - mean) / stdev, 3) for score in total_scores]

        return z_scores

    finally:
        session.close()
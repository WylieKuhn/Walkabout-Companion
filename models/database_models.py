from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker



Base = declarative_base()

class Course(Base):
    """
    Represents a golf course in the database, with individual par columns for each hole.
    """
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    course_name = Column(String, nullable=False, unique=False)
    difficulty = Column(String, nullable=False)

    # Individual columns for par of each hole (up to 18 holes)
    hole_1_par = Column(Integer, nullable=False)
    hole_2_par = Column(Integer, nullable=False)
    hole_3_par = Column(Integer, nullable=False)
    hole_4_par = Column(Integer, nullable=False)
    hole_5_par = Column(Integer, nullable=False)
    hole_6_par = Column(Integer, nullable=False)
    hole_7_par = Column(Integer, nullable=False)
    hole_8_par = Column(Integer, nullable=False)
    hole_9_par = Column(Integer, nullable=False)
    hole_10_par = Column(Integer, nullable=False)
    hole_11_par = Column(Integer, nullable=False)
    hole_12_par = Column(Integer, nullable=False)
    hole_13_par = Column(Integer, nullable=False)
    hole_14_par = Column(Integer, nullable=False)
    hole_15_par = Column(Integer, nullable=False)
    hole_16_par = Column(Integer, nullable=False)
    hole_17_par = Column(Integer, nullable=False)
    hole_18_par = Column(Integer, nullable=False)

    total_par = Column(Integer, nullable=False)

class Game(Base):
    """
    Represents a game of golf in the database, with individual par columns for each hole.
    """
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)  # Primary key, auto-incrementing
    course_name = Column(String, nullable=False, unique=False)  # Name of the course, cannot be null, must be unique
    difficulty = Column(String, nullable=False)  # Difficulty: 'easy' or 'hard'
    player_id = Column(String, nullable=False)
    date = Column(String, nullable=False)
    time = Column(String, nullable=False)
    total_score = Column(Integer, nullable=False)
    putter = Column(String, nullable=False)

    hole_1 = Column(Integer, nullable=False)
    hole_2 = Column(Integer, nullable=False)
    hole_3 = Column(Integer, nullable=False)
    hole_4 = Column(Integer, nullable=False)
    hole_5 = Column(Integer, nullable=False)
    hole_6 = Column(Integer, nullable=False)
    hole_7 = Column(Integer, nullable=False)
    hole_8 = Column(Integer, nullable=False)
    hole_9 = Column(Integer, nullable=False)
    hole_10 = Column(Integer, nullable=False)
    hole_11 = Column(Integer, nullable=False)
    hole_12 = Column(Integer, nullable=False)
    hole_13 = Column(Integer, nullable=False)
    hole_14 = Column(Integer, nullable=False)
    hole_15 = Column(Integer, nullable=False)
    hole_16 = Column(Integer, nullable=False)
    hole_17 = Column(Integer, nullable=False)
    hole_18 = Column(Integer, nullable=False)
import datetime
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from functions.courses import get_courses, get_courses_putter
from models.database_models import Game

engine = create_engine("sqlite:///golfstats2.db")
Session = sessionmaker(bind=engine)
session = Session()

with st.container():
    st.markdown("<h1 style='text-align: center;'>Input Golf Game</h1>", unsafe_allow_html=True)

    with st.form(key="scores"):
        course = st.selectbox(label="Course", options=get_courses(), key="course")
        difficulty = st.selectbox(label="Difficulty", options=["Easy", "Hard"], key="difficulty")
        putter = st.selectbox(label="Putter", options=get_courses_putter())

        col1, col2, col3, col4, col5, col6 = st.columns(6)
        hole_scores = {}

        with col1:
            hole_scores["Hole 1"] = st.number_input(label="Hole 1", min_value=0, step=1, key="1")
            hole_scores["Hole 7"] = st.number_input(label="Hole 7", min_value=0, step=1, key="7")
            hole_scores["Hole 13"] = st.number_input(label="Hole 13", min_value=0, step=1, key="13")
        with col2:
            hole_scores["Hole 2"] = st.number_input(label="Hole 2", min_value=0, step=1, key="2")
            hole_scores["Hole 8"] = st.number_input(label="Hole 8", min_value=0, step=1, key="8")
            hole_scores["Hole 14"] = st.number_input(label="Hole 14", min_value=0, step=1, key="14")
        with col3:
            hole_scores["Hole 3"] = st.number_input(label="Hole 3", min_value=0, step=1, key="3")
            hole_scores["Hole 9"] = st.number_input(label="Hole 9", min_value=0, step=1, key="9")
            hole_scores["Hole 15"] = st.number_input(label="Hole 15", min_value=0, step=1, key="15")
        with col4:
            hole_scores["Hole 4"] = st.number_input(label="Hole 4", min_value=0, step=1, key="4")
            hole_scores["Hole 10"] = st.number_input(label="Hole 10", min_value=0, step=1, key="10")
            hole_scores["Hole 16"] = st.number_input(label="Hole 16", min_value=0, step=1, key="16")
        with col5:
            hole_scores["Hole 5"] = st.number_input(label="Hole 5", min_value=0, step=1, key="5")
            hole_scores["Hole 11"] = st.number_input(label="Hole 11", min_value=0, step=1, key="11")
            hole_scores["Hole 17"] = st.number_input(label="Hole 17", min_value=0, step=1, key="17")
        with col6:
            hole_scores["Hole 6"] = st.number_input(label="Hole 6", min_value=0, step=1, key="6")
            hole_scores["Hole 12"] = st.number_input(label="Hole 12", min_value=0, step=1, key="12")
            hole_scores["Hole 18"] = st.number_input(label="Hole 18", min_value=0, step=1, key="18")
        
        totalStrokes = st.number_input(label="Total Score", min_value=0, step=1, key="total_score")
        date_played = str(st.date_input("Game Date"))
        print(date_played)

        submit_button = st.form_submit_button(label="Log Game")

        if submit_button:

            doubleCheckTotalScore = 0
            for hole, score in hole_scores.items():
                doubleCheckTotalScore += score
            
            if doubleCheckTotalScore == totalStrokes and doubleCheckTotalScore >= 18:
                game_data = {
                    "player_id": 1,
                    "course_name": course,
                    "difficulty": difficulty.lower(),
                    "putter": putter,
                    "total_score": totalStrokes,
                    "date": date_played,
                    "time": datetime.datetime.now().strftime("%H:%M"),
                }

                for i in range(1, 19):
                    game_data[f"hole_{i}"] = hole_scores[f"Hole {i}"]

                new_game = Game(**game_data)
                session.add(new_game)
                session.commit()
                st.success("Game logged successfully!")

            elif doubleCheckTotalScore != totalStrokes:
                if doubleCheckTotalScore > totalStrokes:
                    st.error("You total strokes per hole is greater than your inputted total score. Please check your inputs to ensure accuracy")
                if doubleCheckTotalScore < totalStrokes:
                    st.error("You total strokes per hole is less than your inputted total score. Please check your inputs to ensure accuracy")




import streamlit as st
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd
from functions.compute_z_scores import compute_z_scores
from functions.get_course import get_courses
from functions.games_table import load_table_hole
from functions.create_performance_chart import plot_score_timeseries_hole, plot_score_timeseries_time_hole
from functions.par_averages import percent_under_par_hole
from sqlalchemy import create_engine

engine = create_engine("sqlite:///golfstats2.db")
st.set_page_config(layout="wide")

zScores = [0,0]

average = st.empty()

with st.container():
    zScoreDisplay = st.empty()

    with st.form(key="holestatsform"):
        course = st.selectbox(label="Select Course", options=get_courses())
        difficulty = st.selectbox(label="Difficulty", options=["Easy", "Hard"])
        hole = st.selectbox("Hole", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
        submit = st.form_submit_button(label="See Stats")

        if submit:
            df = load_table_hole(course, difficulty.lower(), hole)
            zScores = compute_z_scores(course, difficulty.lower())
            st_dev = df[f"hole_{hole}"].std()
            variance = df[f"hole_{hole}"].var()

            if not isinstance(df, pd.DataFrame):
                st.warning("No Data To Display, either the returned dataframe is empty or a dataframe has not been loaded by the user")
            
            else:
                st.dataframe(df, use_container_width=True)
                        
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(label="Mean", value=round(df[f"hole_{hole}"].mean(),2))
                    st.metric(label="Chance of beating your best score", value=f"{(1-norm.sf(min(zScores)))*100:.2f}%")
                with col2:
                    st.metric(label="Standard Deviation", value=round(st_dev,2))

                    st.metric(label="Percent Of Times Under Par", value=percent_under_par_hole(course, difficulty.lower(), hole))
                with col3:
                    st.metric(label="Variance", value=round(variance,2))
                    st.metric(label="Times Played", value=df.shape[0])
                
                
                fig, ax = plt.subplots()
                
                plot_score_timeseries_hole(df, hole)
                plot_score_timeseries_time_hole(df, hole)






    
    













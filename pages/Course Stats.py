import sqlite3
import statistics
import streamlit as st
import matplotlib.pyplot as plt
from scipy.stats import norm
import polars as pl
import pandas as pd
from functions.compute_z_scores import compute_z_scores
from functions.get_course import get_courses
from functions.total_scores import total_scores
from functions.games_table import load_table
from functions.create_performance_chart import plot_score_timeseries, plot_score_timeseries_time, distrobution_chart
from functions.par_averages import percent_under_par_course
from sqlalchemy import create_engine

engine = create_engine("sqlite:///golfstats2.db")
st.set_page_config(layout="wide")


totalScores = [0,0]
zScores = [0,0]

average = st.empty()
df = pl.DataFrame()

with st.container():
    zScoreDisplay = st.empty()

    with st.form(key="statsform"):
        course = st.selectbox(label="Select Course", options=get_courses())
        difficulty = st.selectbox(label="Difficulty", options=["Easy", "Hard"])
        submit = st.form_submit_button(label="See Stats")

        if submit:
            df = load_table(course, difficulty.lower())
            zScores = compute_z_scores(course, difficulty.lower())
            totalScores = total_scores(course, difficulty.lower())
            

        if not isinstance(df, pd.DataFrame):
            st.warning("No Data To Display, either the returned dataframe is empty or a dataframe has not been loaded by the user")
        
        else:
            st.dataframe(df, use_container_width=True)
                    
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(label="Mean", value=round(statistics.mean(totalScores),2))
                st.metric(label="Chance of beating your best score", value=f"{(1-norm.sf(min(zScores)))*100:.2f}%")
                distrobution_chart(df)
            with col2:
                st.metric(label="Standard Deviation", value=round(statistics.pstdev(totalScores),2))

                st.metric(label="Percent Of Games Under Par", value=percent_under_par_course(course, difficulty))
            with col3:
                st.metric(label="Variance", value=round(statistics.variance(totalScores),2))
                st.metric(label="Times Played", value=df.shape[0])
            
        
            
            plot_score_timeseries(df)
            plot_score_timeseries_time(df)






    
    













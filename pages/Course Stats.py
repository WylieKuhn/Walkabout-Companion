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
from functions.create_performance_chart import plot_score_timeseries


st.set_page_config(layout="wide")

conn = sqlite3.connect("golfstats.db")
cur = conn.cursor()
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
            df = load_table(course, difficulty)
            print("dataframe is", df)
            zScores = compute_z_scores(course, difficulty)
            totalScores = total_scores(course, difficulty)
            

        if not isinstance(df, pd.DataFrame):
            st.error("No Data To Display")
        
        else:
            st.dataframe(df, use_container_width=True)
                    
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(label="Mean", value=round(statistics.mean(totalScores),2))
                st.text("Chance of beating your best score",)

                st.text(f"{(1-norm.sf(min(zScores)))*100:.2f}%")
                
            with col2:
                st.metric(label="Standard Deviation", value=round(statistics.pstdev(totalScores),2))

                fig, ax = plt.subplots()
                ax.hist(zScores, bins=50)
                st.text("Normal Distrobution")
                st.pyplot(fig)

            with col3:
                st.metric(label="Variance", value=round(statistics.variance(totalScores),2))

            
            plot_score_timeseries(df)






    
    













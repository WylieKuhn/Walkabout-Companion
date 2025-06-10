import sqlite3
import pandas as pd
import streamlit as st
from functions.dataframe_functions import convert_date_to_object

st.set_page_config(layout="wide")
conn = sqlite3.connect("golfstats.db")

query = "SELECT * FROM games"
df = pd.read_sql_query(query, conn)

df = convert_date_to_object(df)


best_game = df.loc[df['total_score'].idxmin()].to_dict()
worst_game = df.loc[df['total_score'].idxmax()].to_dict()

averages = (
    df.groupby(["course", "difficulty"])  # Group by the specified columns
      .agg(avg_score=('total_score', 'mean')) # Calculate the mean of 'total_score' and name it 'avg_score'
      .reset_index()                      # Convert the grouped columns from index back to regular columns
      .sort_values(by="avg_score")        # Sort the results by 'avg_score'
)

best_easy = averages[averages['difficulty'].str.lower() == 'easy'].iloc[0].to_dict()
best_hard = averages[averages['difficulty'].str.lower() == 'hard'].iloc[0].to_dict()

play_counts_pandas = df['course'].value_counts().reset_index()
play_counts_pandas.columns = ['course', 'count']


most_played = play_counts_pandas.iloc[0].to_dict()
least_played = play_counts_pandas.iloc[-1].to_dict()

st.title("User Golf Stats Summary")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Best Game")
    st.markdown(f"""
    **Course:** {best_game['course']}  
    **Score:** {best_game['total_score']}  
    **Date:** {best_game['date']}
    """)
    
    st.subheader("Best Game (Strokes Under Par)")

    st.subheader("Best Easy Course (Avg Score)")
    st.markdown(f"""
    **Course:** {best_easy['course']}  
    **Avg Score:** {round(best_easy['avg_score'], 2)}
    """)

    st.subheader("Most Played Course")
    st.markdown(f"""
    **Course:** {most_played['course']}  
    **Rounds Played:** {most_played['count']}
    """)

with col2:
    st.subheader("Worst Game")
    st.markdown(f"""
    **Course:** {worst_game['course']}  
    **Score:** {worst_game['total_score']}  
    **Date:** {worst_game['date']}
    """)

    st.subheader("Best Hard Course (Avg Score)")
    st.markdown(f"""
    **Course:** {best_hard['course']}  
    **Avg Score:** {round(best_hard['avg_score'], 2)}
    """)

    st.subheader("Least Played Course")
    st.markdown(f"""
    **Course:** {least_played['course']}  
    **Rounds Played:** {least_played['count']}
    """)

st.subheader("Course Play Frequency")
play_counts = df['course'].value_counts().reset_index()

st.bar_chart(play_counts.set_index("course")["count"])


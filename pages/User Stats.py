import sqlite3
import pandas as pd
import streamlit as st
from functions.dataframe_functions import load_courses_dataframe, load_games_dataframe

st.set_page_config(layout="wide")
db = "golfstats.db"

query = "SELECT * FROM games"
games_df = load_games_dataframe(db)
courses_df = load_courses_dataframe(db)
games_df['total_score'] = pd.to_numeric(games_df['total_score'])
merged_df = pd.merge(games_df, courses_df, left_on="name", right_on="name")
merged_df["over_under_easy"] = merged_df["total_score"] - merged_df["easy"]
merged_df["over_under_hard"] = merged_df["total_score"] - merged_df["hard"]

best_game = games_df.loc[games_df['total_score'].idxmin()].to_dict()
worst_game = games_df.loc[games_df['total_score'].idxmax()].to_dict()

averages = (
    games_df.groupby(["name", "difficulty"])  # Group by the specified columns
      .agg(avg_score=('total_score', 'mean')) # Calculate the mean of 'total_score' and name it 'avg_score'
      .reset_index()                      # Convert the grouped columns from index back to regular columns
      .sort_values(by="avg_score")        # Sort the results by 'avg_score'
)

best_easy = averages[averages['difficulty'].str.lower() == 'easy'].iloc[0].to_dict()
best_hard = averages[averages['difficulty'].str.lower() == 'hard'].iloc[0].to_dict()

play_counts_pandas = games_df['name'].value_counts().reset_index()
play_counts_pandas.columns = ['name', 'count']

most_played = play_counts_pandas.iloc[0].to_dict()
least_played = play_counts_pandas.iloc[-1].to_dict()

merged_df.sort_values("over_under_easy")
most_under_easy = merged_df.loc[merged_df["over_under_easy"].idxmin()]
most_under_hard = merged_df.loc[merged_df["over_under_hard"].idxmin()]

most_over_easy = merged_df.loc[merged_df["over_under_easy"].idxmax()]
most_over_hard = merged_df.loc[merged_df["over_under_hard"].idxmax()]

st.title("User Golf Stats Summary")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Best Game")
    st.markdown(f"""
    **Course:** {best_game['name']}  
    **Score:** {best_game['total_score']}  
    **Date:** {best_game['date']}
    """)
    
    st.subheader("Best Easy Course (Relative To Par)")
    st.markdown(f"""
    **Course:** {most_under_easy["name"]}  
    **Date:** {most_under_easy["date"]}  
    **Time** {most_under_easy["time"]}  
    **Score Relative To Par:** {most_under_easy["over_under_easy"]}  
    """)

    st.subheader("Worst Easy Course (Relative To Par)")
    st.markdown(f"""
    **Course:** {most_over_easy["name"]}  
    **Date:** {most_over_easy["date"]}  
    **Time** {most_over_easy["time"]}  
    **Score Relative To Par:** {most_over_easy["over_under_hard"]}
    """)

    st.subheader("Best Easy Course (Avg Score)")
    st.markdown(f"""
    **Course:** {best_easy['name']}  
    **Avg Score:** {round(best_easy['avg_score'], 2)}
    """)

    st.subheader("Most Played Course")
    st.markdown(f"""
    **Course:** {most_played['name']}  
    **Rounds Played:** {most_played['count']}
    """)

with col2:
    st.subheader("Worst Game")
    st.markdown(f"""
    **Course:** {worst_game['name']}  
    **Score:** {worst_game['total_score']}  
    **Date:** {worst_game['date']}
    """)

    st.subheader("Best Hard Course (Relative To Par)")
    st.markdown(f"""
    **Course:** {most_under_hard["name"]}  
    **Date:** {most_under_hard["date"]}  
    **Time** {most_under_hard["time"]}  
    **Score Relative To Par:** {most_under_hard["over_under_hard"]}
    """)

    st.subheader("Worst Hard Course (Relative To Par)")
    st.markdown(f"""
    **Course:** {most_over_hard["name"]}  
    **Date:** {most_over_hard["date"]}  
    **Time** {most_over_hard["time"]}  
    **Score Relative To Par:** {most_over_hard["over_under_hard"]}
    """)

    st.subheader("Best Hard Course (Avg Score)")
    st.markdown(f"""
    **Course:** {best_hard['name']}  
    **Avg Score:** {round(best_hard['avg_score'], 2)}
    """)

    st.subheader("Least Played Course")
    st.markdown(f"""
    **Course:** {least_played['name']}  
    **Rounds Played:** {least_played['count']}
    """)

st.subheader("Course Play Frequency")
play_counts = games_df['name'].value_counts().reset_index()


st.bar_chart(play_counts.set_index("name")["count"])

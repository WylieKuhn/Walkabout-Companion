import sqlite3
import polars as pl
import streamlit as st

st.set_page_config(layout="wide")
conn = sqlite3.connect("golfstats.db")
cur = conn.cursor()

query = "SELECT * FROM games"
rows = cur.execute(query).fetchall()
columns = [desc[0] for desc in cur.description]
df = pl.DataFrame(rows, schema=columns)

df = df.with_columns([
    pl.col("date").str.strptime(pl.Date, "%Y-%m-%d"),
    pl.col("total_score").cast(pl.Int32)
])

best_game = df.sort("total_score").slice(0, 1).to_dicts()[0]
worst_game = df.sort("total_score", descending=True).slice(0, 1).to_dicts()[0]

averages = (
    df.group_by(["course", "difficulty"])
      .agg(pl.col("total_score").mean().alias("avg_score"))
      .sort("avg_score")
)

best_easy = averages.filter(pl.col("difficulty") == "Easy").slice(0, 1).to_dicts()[0]
best_hard = averages.filter(pl.col("difficulty") == "Hard").slice(0, 1).to_dicts()[0]

play_counts = df.group_by("course").count().sort("count", descending=True)
most_played = play_counts.slice(0, 1).to_dicts()[0]
least_played = play_counts.slice(-1, 1).to_dicts()[0]

st.title("User Golf Stats Summary")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Best Game")
    st.markdown(f"""
    **Course:** {best_game['course']}  
    **Score:** {best_game['total_score']}  
    **Date:** {best_game['date']}
    """)

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
st.bar_chart(play_counts.to_pandas().set_index("course")["count"])


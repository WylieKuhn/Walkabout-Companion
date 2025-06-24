import pandas as pd
import streamlit as st

def plot_score_timeseries(df: pd.DataFrame):
  course_df = df[["date", "total_score"]].sort_values(by='date')
  course_df.set_index("date", inplace=True)

  st.subheader("Score Over Time")
  st.scatter_chart(course_df)

def plot_score_timeseries_time(df: pd.DataFrame):
  course_df = df[["time", "total_score"]].sort_values(by="time")
  course_df["time"] = pd.to_datetime(course_df["time"].astype(str), format="%H:%M:%S")

  st.subheader("Score By Time Of Day")
  st.scatter_chart(data=course_df, x="time", y="total_score")

def plot_score_timeseries_hole(df: pd.DataFrame, hole_number: int):
  hole_col = f"hole_{hole_number}"

  if hole_col not in df.columns:
      st.error(f"No data available for Hole {hole_number}")
      return

  course_df = df[["date", hole_col]].sort_values(by="date")
  course_df.rename(columns={hole_col: "score"}, inplace=True)

  st.subheader(f"Score Over Time - Hole {hole_number}")
  st.scatter_chart(data=course_df, x="date", y="score")

def plot_score_timeseries_time_hole(df: pd.DataFrame, hole_number: int):
    hole_col = f"hole_{hole_number}"

    if hole_col not in df.columns:
        st.error(f"No data available for Hole {hole_number}")
        return

    course_df = df[["time", hole_col]].copy()
    course_df.rename(columns={hole_col: "score"}, inplace=True)

    course_df["time"] = pd.to_datetime(course_df["time"].astype(str), format="%H:%M:%S")

    course_df.sort_values(by="time", inplace=True)

    st.subheader(f"Score by Time of Day - Hole {hole_number}")
    st.scatter_chart(data=course_df, x="time", y="score")

def distrobution_chart(df: pd.DataFrame):
    score_counts = df["total_score"].value_counts().sort_index()

    plot_df = pd.DataFrame({
        "total_score": score_counts.index,
        "count": score_counts.values
    }).set_index("total_score")

    st.subheader("Distribution of Total Scores")
    st.bar_chart(plot_df["count"])


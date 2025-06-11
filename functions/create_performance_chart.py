import pandas as pd
import streamlit as st

def plot_score_timeseries(df: pd.DataFrame):
  course_df = df[["date", "total_score"]].sort_values(by='date')
  course_df.set_index("date", inplace=True)

  st.subheader("Score Over Time")
  st.scatter_chart(course_df)

def plot_score_timeseries_time(df: pd.DataFrame):
  course_df = df[["time", "total_score"]].sort_values(by='time')
  course_df.set_index("time", inplace=True)

  st.subheader("Score By Time Of Day")
  st.scatter_chart(course_df)

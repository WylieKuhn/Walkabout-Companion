import pandas as pd
import pandas as pd
import streamlit as st

def plot_score_timeseries(df: pd.DataFrame):
  course_df = df[["date", "total_score"]].sort_values(by='date')
  course_df.set_index("date", inplace=True)

  st.subheader("Score Over Time")
  st.scatter_chart(course_df)

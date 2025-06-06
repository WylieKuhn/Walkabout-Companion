import polars as pl
import pandas as pd
import streamlit as st

def plot_score_timeseries(df: pl.DataFrame):
    course_df = (
        df.select(["date", "total_score"])
          .sort("date")
    )
    pd_df = course_df.to_pandas()

    pd_df["date"] = pd.to_datetime(pd_df["date"])

    pd_df.set_index("date", inplace=True)

    st.subheader("Score Over Time")
    st.line_chart(pd_df)

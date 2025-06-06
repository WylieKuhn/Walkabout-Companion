import polars as pl
import pandas as pd
import streamlit as st

def plot_score_timeseries(df: pl.DataFrame):
    # Filter for selected course assumed already done outside
    # Just select needed columns and sort
    course_df = (
        df.select(["date", "total_score"])
          .sort("date")
    )

    # Convert to Pandas
    pd_df = course_df.to_pandas()

    # Ensure 'date' is datetime
    pd_df["date"] = pd.to_datetime(pd_df["date"])

    # Set date as index
    pd_df.set_index("date", inplace=True)

    # Plot
    st.subheader("Score Over Time")
    st.line_chart(pd_df)

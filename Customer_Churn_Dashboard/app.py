import streamlit as st

st.set_page_config(
    page_title="Customer Segmentation & Churn Analytics",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Customer Segmentation & Churn Analytics")
st.markdown("### European Banking Dataset")

st.write(
"""
This dashboard analyzes customer churn patterns across European banks.

Use the pages on the left to explore:

- Customer Overview
- Customer Segmentation
- Churn Analysis
- Business Insights
"""
)

st.info("Select a page from the sidebar.")
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("👥 Customer Segmentation")

# Load dataset
df = pd.read_csv("European_Bank (1).csv")

# Sidebar filters
st.sidebar.header("Filters")

country = st.sidebar.multiselect(
    "Select Country",
    options=df["Geography"].unique(),
    default=df["Geography"].unique()
)

gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

# Apply filters
filtered_df = df[
    (df["Geography"].isin(country)) &
    (df["Gender"].isin(gender))
]


filtered_df["AgeGroup"] = pd.cut(
    filtered_df["Age"],
    bins=[18,30,40,50,60,100],
    labels=[
        "18-30",
        "31-40",
        "41-50",
        "51-60",
        "60+"
    ]
)

age_count = (
    filtered_df["AgeGroup"]
    .value_counts()
    .sort_index()
    .reset_index()
)

age_count.columns = ["Age Group","Customers"]

fig = px.bar(
    age_count,
    x="Age Group",
    y="Customers",
    color="Customers",
    text="Customers",
    color_continuous_scale="Blues"
)

fig.update_layout(
    title="Customer Distribution by Age Group"
)

st.plotly_chart(fig,use_container_width=True)

geo = (
    filtered_df["Geography"]
    .value_counts()
    .reset_index()
)

geo.columns = ["Country","Customers"]

fig = px.pie(
    geo,
    names="Country",
    values="Customers",
    hole=0.45
)

fig.update_layout(
    title="Customer Distribution by Country"
)

st.plotly_chart(fig,use_container_width=True)

gender_df = (
    filtered_df["Gender"]
    .value_counts()
    .reset_index()
)

gender_df.columns = ["Gender","Customers"]

fig = px.bar(
    gender_df,
    x="Gender",
    y="Customers",
    color="Gender",
    text="Customers"
)

fig.update_layout(
    title="Customer Distribution by Gender"
)

st.plotly_chart(fig,use_container_width=True)

st.subheader("Filtered Dataset")

st.dataframe(filtered_df)
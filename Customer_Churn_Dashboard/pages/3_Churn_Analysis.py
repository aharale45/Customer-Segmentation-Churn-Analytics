import streamlit as st
import plotly.express as px
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "European_Bank (1).csv"

df = pd.read_csv(DATA_FILE)

st.title("📉 Churn Analysis")

# Load Dataset


st.sidebar.header("Filters")

country = st.sidebar.multiselect(
    "Country",
    df["Geography"].unique(),
    default=df["Geography"].unique()
)

gender = st.sidebar.multiselect(
    "Gender",
    df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[
    (df["Geography"].isin(country)) &
    (df["Gender"].isin(gender))
]

total = len(filtered_df)

churned = filtered_df["Exited"].sum()

retained = total - churned

rate = round(churned / total * 100, 2)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Customers", total)

c2.metric("Churned", churned)

c3.metric("Retained", retained)

c4.metric("Churn Rate", f"{rate}%")

country_churn = (
    filtered_df.groupby("Geography")["Exited"]
    .mean()
    .reset_index()
)

country_churn["Exited"] *= 100

fig = px.bar(
    country_churn,
    x="Geography",
    y="Exited",
    text=country_churn["Exited"].round(1),
    color="Exited",
    color_continuous_scale="Reds"
)

fig.update_layout(
    title="Customer Churn Rate by Country",
    xaxis_title="Country",
    yaxis_title="Churn Rate (%)"
)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

gender_churn = (
    filtered_df.groupby("Gender")["Exited"]
    .mean()
    .reset_index()
)

gender_churn["Exited"] *= 100

fig = px.bar(
    gender_churn,
    x="Gender",
    y="Exited",
    color="Gender",
    text=gender_churn["Exited"].round(1)
)

fig.update_layout(
    title="Customer Churn Rate by Gender",
    yaxis_title="Churn Rate (%)"
)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

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

age = (

    filtered_df.groupby("AgeGroup")["Exited"]

    .mean()

    .reset_index()

)

age["Exited"] *= 100

fig = px.bar(

    age,

    x="AgeGroup",

    y="Exited",

    color="Exited",

    text=age["Exited"].round(1),

    color_continuous_scale="Oranges"

)

fig.update_layout(

    title="Customer Churn by Age Group",

    xaxis_title="Age Group",

    yaxis_title="Churn Rate (%)"

)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

activity = (

    filtered_df.groupby("IsActiveMember")["Exited"]

    .mean()

    .reset_index()

)

activity["Exited"] *= 100

activity["IsActiveMember"] = activity["IsActiveMember"].replace({

    0: "Inactive",

    1: "Active"

})

fig = px.bar(

    activity,

    x="IsActiveMember",

    y="Exited",

    color="IsActiveMember",

    text=activity["Exited"].round(1)

)

fig.update_layout(

    title="Customer Churn by Activity Status",

    xaxis_title="Customer Status",

    yaxis_title="Churn Rate (%)",

    showlegend=False

)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

filtered_df["Status"] = filtered_df["Exited"].replace({

    0: "Retained",

    1: "Exited"

})

fig = px.box(

    filtered_df,

    x="Status",

    y="Balance",

    color="Status"

)

fig.update_layout(

    title="Account Balance Distribution by Churn"

)

st.plotly_chart(fig, use_container_width=True)

year = (

    filtered_df.groupby("Year")["Exited"]

    .mean()

    .reset_index()

)

year["Exited"] *= 100

fig = px.line(

    year,

    x="Year",

    y="Exited",

    markers=True

)

fig.update_layout(

    title="Year-wise Customer Churn Trend",

    xaxis_title="Year",

    yaxis_title="Churn Rate (%)"

)

st.plotly_chart(fig, use_container_width=True)

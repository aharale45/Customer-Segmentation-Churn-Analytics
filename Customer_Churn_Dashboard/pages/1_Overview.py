import streamlit as st
import pandas as pd

st.title("📊 Customer Overview")

df = pd.read_csv("European_Bank (1).csv")

total_customers = len(df)

churn_rate = round(df['Exited'].mean()*100,2)

avg_balance = round(df['Balance'].mean(),2)

avg_credit = round(df['CreditScore'].mean(),2)

col1,col2,col3,col4=st.columns(4)

col1.metric("Customers",total_customers)

col2.metric("Churn Rate",str(churn_rate)+" %")

col3.metric("Avg Balance",f"${avg_balance:,.0f}")

col4.metric("Avg Credit Score",avg_credit)


import plotly.express as px

churn=df['Exited'].value_counts().reset_index()

churn.columns=['Status','Count']

churn['Status']=churn['Status'].replace(
{
0:'Retained',
1:'Exited'
}
)

fig=px.pie(

churn,

names='Status',

values='Count',

hole=.45,

color='Status',

color_discrete_sequence=['royalblue','crimson']

)

fig.update_layout(

title="Overall Customer Churn"

)

st.plotly_chart(fig,use_container_width=True)
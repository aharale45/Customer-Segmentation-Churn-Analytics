import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📌 Business Insights & Recommendations")

# Load Dataset
df = pd.read_csv("European_Bank (1).csv")

# Overall KPIs
total_customers = len(df)

churned_customers = df["Exited"].sum()

churn_rate = round((churned_customers / total_customers) * 100, 2)

avg_balance = round(df["Balance"].mean(), 2)

avg_credit = round(df["CreditScore"].mean(), 2)

active_rate = round(df["IsActiveMember"].mean() * 100, 2)

c1, c2, c3 = st.columns(3)

c1.metric("Total Customers", total_customers)

c2.metric("Overall Churn Rate", f"{churn_rate}%")

c3.metric("Average Balance", f"${avg_balance:,.0f}")

c4, c5 = st.columns(2)

c4.metric("Average Credit Score", avg_credit)

c5.metric("Active Customers", f"{active_rate}%")

country = df.groupby("Geography")["Exited"].mean().sort_values(ascending=False)

highest_country = country.index[0]

highest_rate = round(country.iloc[0] * 100, 2)

st.success(
    f"🏆 Highest Churn Country: **{highest_country}** ({highest_rate}%)"
)

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[18,30,40,50,60,100],
    labels=["18-30","31-40","41-50","51-60","60+"]
)

age = df.groupby("AgeGroup")["Exited"].mean().sort_values(ascending=False)

highest_age = age.index[0]

highest_age_rate = round(age.iloc[0] * 100,2)

st.info(
    f"👥 Highest Churn Age Group: **{highest_age}** ({highest_age_rate}%)"
)

high_value = df[df["Balance"] >= 100000]

hv_rate = round(high_value["Exited"].mean() * 100, 2)

st.warning(
    f"💰 High Value Customer Churn Rate: **{hv_rate}%**"
)

activity = df.groupby("IsActiveMember")["Exited"].mean()

inactive = round(activity[0] * 100, 2)

active = round(activity[1] * 100, 2)

st.write("### Customer Activity Analysis")

st.write(f"✅ Active Customers Churn Rate: **{active}%**")

st.write(f"❌ Inactive Customers Churn Rate: **{inactive}%**")

st.subheader("Top 5 Customers by Account Balance")

top_balance = (
    df.sort_values("Balance", ascending=False)
      [["CustomerId", "Geography", "Balance", "Exited"]]
      .head(5)
)

st.dataframe(top_balance)

st.subheader("📋 Recommendations")

st.markdown("""
### Recommended Retention Strategies

- Focus customer retention campaigns in countries with the highest churn.
- Introduce loyalty programs for customers with high account balances.
- Improve engagement with inactive members using personalized offers.
- Monitor middle-aged and senior customer segments more closely.
- Strengthen customer relationship management for premium customers.
- Promote cross-selling to customers with only one product.
- Regularly monitor churn trends using interactive dashboards.
""")

st.subheader("📖 Conclusion")

st.write("""
The dashboard provides a comprehensive analysis of customer churn in European banking using demographic, financial, and behavioral data.

Key findings include:
- Significant differences in churn across countries.
- Higher churn among inactive customers.
- Increased churn in older customer segments.
- High-value customers require targeted retention strategies.

The dashboard enables management to identify high-risk customer groups and supports data-driven decision-making for customer retention and business growth.
""")


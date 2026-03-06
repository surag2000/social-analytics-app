import streamlit as st
import pandas as pd
import plotly.express as px

# App title
st.title("Social Media Analytics Dashboard")
st.write("Welcome to your analytics app!")

# File upload
st.subheader("Upload Your Data")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Load data - use uploaded file or fall back to sample data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Your file was uploaded successfully!")
else:
    df = pd.read_csv("sample_data.csv")
    st.info("ℹ️ Using sample data. Upload your own CSV above to see your real stats!")


# Sidebar filters
st.sidebar.title("Filters")
platforms = df["platform"].unique().tolist()
selected_platform = st.sidebar.multiselect("Select Platform", platforms, default=platforms)

# Filter the data
df = df[df["platform"].isin(selected_platform)]

# Summary metric cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Posts", len(df))
col2.metric("Total Likes", df["likes"].sum())
col3.metric("Total Reach", df["reach"].sum())
col4.metric("Avg Engagement Rate", f"{((df['likes'] + df['comments'] + df['shares']) / df['reach'] * 100).mean().round(2)}%")

# Show the raw data
st.subheader("Raw Data")
st.dataframe(df)

# Chart 1 - Likes by Platform
st.subheader("Likes by Platform")
fig = px.bar(df, x="platform", y="likes", color="platform", title="Total Likes per Platform")
st.plotly_chart(fig)

# Chart 2 - Engagement over Time
st.subheader("Engagement Over Time")
fig2 = px.line(df, x="date", y="likes", color="platform", title="Likes Over Time by Platform")
st.plotly_chart(fig2)

# Chart 3 - Reach vs Impressions
st.subheader("Reach vs Impressions")
fig3 = px.scatter(df, x="reach", y="impressions", color="platform", size="likes", title="Reach vs Impressions")
st.plotly_chart(fig3)

# Engagement Rate Calculator
st.subheader("Engagement Rate by Post")
df["engagement_rate"] = ((df["likes"] + df["comments"] + df["shares"]) / df["reach"] * 100).round(2)
st.dataframe(df[["date", "platform", "post_type", "engagement_rate"]])

# Best performing post
best_post = df.loc[df["engagement_rate"].idxmax()]
st.success(f"🏆 Best Post: {best_post['platform']} {best_post['post_type']} on {best_post['date']} with {best_post['engagement_rate']}% engagement rate")

# Best Day to Post
st.subheader("Best Day to Post")
df["date"] = pd.to_datetime(df["date"])
df["day_of_week"] = df["date"].dt.day_name()
day_engagement = df.groupby("day_of_week")["engagement_rate"].mean().reset_index()
fig4 = px.bar(day_engagement, x="day_of_week", y="engagement_rate",
              title="Average Engagement Rate by Day",
              color="engagement_rate",
              color_continuous_scale="greens")
st.plotly_chart(fig4)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sarlavha
st.title("Betting Analysis Tool")
st.write("📊 This app analyzes sample betting data (for research purposes only).")

# Sample data
data = {
    "Team": ["Team A", "Team B", "Team C", "Team D"],
    "Matches": [20, 18, 22, 25],
    "Wins": [12, 9, 11, 18]
}

df = pd.DataFrame(data)
df["Win Rate"] = df["Wins"] / df["Matches"]

# Show data
st.subheader("Raw Data")
st.dataframe(df)

# Bar chart
st.subheader("Win Rate by Team")
fig, ax = plt.subplots()
ax.bar(df["Team"], df["Win Rate"], color="skyblue")
ax.set_ylabel("Win Rate")
st.pyplot(fig)

# User input
st.subheader("Simulate Match Odds")
team = st.selectbox("Choose a team", df["Team"])
odds = round(float(df[df["Team"] == team]["Win Rate"]) * 100, 2)
st.write(f"📈 Estimated winning chance for **{team}**: {odds}%")

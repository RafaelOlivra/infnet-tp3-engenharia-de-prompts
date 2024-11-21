import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title and subtitle of the app
st.title("Sentiment Analysis of Simpsons Episode 92")
st.subheader("Pizza Chart Visualization of Sentiment Classification")

# Load the CSV file
data = pd.read_csv('./data/03_processed/simpsons_ep92_sentiment_analysis.csv', delimiter=';')

# Count the occurrences of each sentiment
sentiment_counts = data['sentiment'].value_counts()

# Create a pizza chart
fig, ax = plt.subplots()
ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart in the Streamlit app
st.pyplot(fig)
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.load_data import load_cleaned_data
import plotly.express as px
from PIL import Image

# Header Image
image_path = "static/images/fT_corr_header.jpg"
output_path = "static/images/ft_corr_header_converted.jpg"

try:
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img = img.resize((600, 200))
        img.save(output_path, format="PNG")
except Exception as e:
    print(f"Error processing image: {e}")

st.image(output_path, use_container_width=True)

# Title & Intro
st.title("Feature Correlation Analysis")
st.markdown("""
Explore how different property attributes correlate with house sale prices.
Correlation values:
- **+1** = strong positive
- **-1** = strong negative
- **0** = no correlation
---
""")

# Load Data
try:
    df = pd.read_csv("data/processed/final/x_test.csv")
    y = pd.read_csv("data/processed/final/y_test.csv")
    df["LogSalePrice"] = y["LogSalePrice"]
    st.write(f"Dataset: **{df.shape[0]} rows** × **{df.shape[1]} columns**")
    st.dataframe(df.head())

    # Correlation matrix
    corr_matrix = df.corr()

# Plot heatmap for top correlated features
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df[top_features].corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
st.pyplot(fig)

# Feature selector and scatter plot
st.subheader("Scatter Plot Explorer")

feature = st.selectbox("Choose a feature to compare against LogSalePrice", top_features[1:])  # skip LogSalePrice

fig2, ax2 = plt.subplots()
sns.scatterplot(x=df[feature], y=df['LogSalePrice'], ax=ax2)
ax2.set_xlabel(feature)
ax2.set_ylabel("LogSalePrice")
st.pyplot(fig2)

import pandas as pd

def load_cleaned_data(path='data/processed/df_cleaned.csv'):
    return pd.read_csv(path)

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utils.load_data import load_cleaned_data

st.title("Feature Correlation Analysis")
st.write("This page helps visualize how different numerical features relate to the target variable `LogSalePrice`.")

# Load data
df = load_cleaned_data()

# Select numeric features + correlation matrix
# Filter numeric columns
numeric_df = df.select_dtypes(include='number')

# Calculate correlation with LogSalePrice
corr_matrix = numeric_df.corr()

# Select correlations with LogSalePrice only
target_corr = corr_matrix['LogSalePrice'].sort_values(ascending=False)

# Plot full correlation heatmap
st.subheader("Correlation Heatmap")

top_n = st.slider("Select Top N Features by Correlation with LogSalePrice", 5, 30, 10)

top_features = target_corr.head(top_n).index.tolist()

# Plot heatmap for top correlated features
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df[top_features].corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
st.pyplot(fig)

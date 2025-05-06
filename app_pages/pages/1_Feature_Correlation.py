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


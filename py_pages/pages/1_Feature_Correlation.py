import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.load_data import load_cleaned_data
import plotly.express as px
from PIL import Image

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

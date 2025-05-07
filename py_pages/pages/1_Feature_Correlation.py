import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.load_data import load_cleaned_data
import plotly.express as px
from PIL import Image

# Header Image
image_path = "static/images/ft_corr_header.jpg"
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

    # Heatmap Toggle
    st.header("Feature Correlation Heatmap")
    heatmap_type = st.radio("Choose view:", ["Standard Heatmap", "Custom Heatmap"])

    if heatmap_type == "Standard Heatmap":
        fig = px.imshow(corr_matrix, title="Full Correlation Matrix", text_auto=".2f", width=1000, height=800)
        st.plotly_chart(fig)

    elif heatmap_type == "Custom Heatmap":
        features = st.multiselect("Select features:", df.columns.tolist(), default=["LogSalePrice"])
        if len(features) > 1:
            fig = px.imshow(df[features].corr(), title="Custom Correlation Heatmap", text_auto=".2f", width=1000, height=800)
            st.plotly_chart(fig)
        else:
            st.warning("Select at least two features.")

    # Bar Chart: Top Correlation
    st.subheader("Top Correlated Features")
    top_n = st.slider("How many top features to show?", 5, 30, 10)
    top_corr = corr_matrix["LogSalePrice"].drop("LogSalePrice").abs().sort_values(ascending=False).head(top_n)
    fig = px.bar(
        x=top_corr.values,
        y=top_corr.index,
        orientation='h',
        labels={"x": "Correlation", "y": "Feature"},
        title="Top Correlated Features with LogSalePrice",
        color=top_corr.values,
        color_continuous_scale="Teal"
    )
    st.plotly_chart(fig)

    # Pairplot Section
    st.subheader("🔗 Feature Pair Relationships")
    pairplot_features = st.multiselect("Choose features to plot", top_corr.index.tolist(), default=top_corr.index[:3].tolist())

    if pairplot_features:
        fig = px.scatter_matrix(df, dimensions=pairplot_features + ["LogSalePrice"], color="LogSalePrice")
        st.plotly_chart(fig)

    # Insights
    st.header("Key Insights")
    st.markdown("""
- **Overall Quality** and **GrLivArea** are top predictors of price.
- **GarageArea**, **1stFlrSF**, and **LotArea** show moderate positive influence.
- Weak or negative features may introduce noise or multicollinearity.
- Use this analysis to guide feature selection for your model.
""")

except FileNotFoundError:
    st.error("Could not find processed correlation dataset. Check your file path.")

except Exception as e:
    st.error(f"Error during correlation analysis: {e}")
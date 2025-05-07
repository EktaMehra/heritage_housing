import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import os
import sys
import numpy as np

# Ensure parent dir is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- PAGE CONFIG ---
st.set_page_config(page_title="Feature Correlation", layout="wide")

# --- HEADER IMAGE ---
image_path = "static/images/ft_corr_header.jpg"
output_path = "static/images/ft_corr_header_converted.png"

try:
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img = img.resize((600, 200))
        img.save(output_path, format="PNG")
    st.image(output_path, use_container_width=True)
except Exception as e:
    st.warning(f"Image not loaded: {e}")

# --- PAGE TITLE ---
st.title("Feature Correlation Analysis")
st.markdown("""
Explore how different property attributes correlate with house sale prices.
Correlation values:
- **+1** = strong positive
- **-1** = strong negative
- **0** = no correlation
---
""")

# --- LOAD DATA ---
try:
    df = pd.read_csv("data/processed/final/X_test.csv")
    y = pd.read_csv("data/processed/final/y_test.csv")
    df["LogSalePrice"] = np.log1p(y.iloc[:, 0])

    st.write(f"Dataset: **{df.shape[0]} rows** × **{df.shape[1]} columns**")
    st.dataframe(df.head())

    corr_matrix = df.corr()

    # --- HEATMAP TOGGLE ---
    st.header("Feature Correlation Heatmap")
    heatmap_type = st.radio("Select heatmap type:", ["Standard Heatmap", "Custom Heatmap"])

    if heatmap_type == "Standard Heatmap":
        fig = px.imshow(
            corr_matrix,
            title="Full Correlation Matrix",
            text_auto=".2f",
            width=1000,
            height=800,
            color_continuous_scale="Viridis",
        )
        st.plotly_chart(fig)

    elif heatmap_type == "Custom Heatmap":
        features = st.multiselect(
            "Select features to compare:",
            options=df.columns.tolist(),
            default=["LogSalePrice", "overallqual", "grlivarea"]
        )
        if len(features) > 1:
            fig = px.imshow(
                df[features].corr(),
                title="Custom Correlation Heatmap",
                text_auto=".2f",
                width=1000,
                height=800,
                color_continuous_scale="Viridis"
            )
            st.plotly_chart(fig)
        else:
            st.warning("Please select at least two features.")

    # --- BAR CHART: TOP CORRELATIONS ---
    st.subheader("📊 Top Features Correlated with LogSalePrice")
    top_n = st.slider("Number of features to display:", 5, 30, 10)

    top_corr = corr_matrix["LogSalePrice"].drop("LogSalePrice").sort_values(key=abs, ascending=False).head(top_n)

    fig = px.bar(
        x=top_corr.values,
        y=top_corr.index,
        orientation='h',
        labels={"x": "Correlation", "y": "Feature"},
        title="Top Correlated Features",
        color=top_corr.values,
        color_continuous_scale="Teal"
    )
    fig.update_layout(height=500)
    fig.update_traces(hovertemplate="%{y}: %{x:.2f}")
    st.plotly_chart(fig)

    # --- SCATTER MATRIX / PAIR PLOT ---
    st.subheader("🔗 Feature Pair Relationships")
    pairplot_features = st.multiselect(
        "Select features for pairwise scatter matrix:",
        options=top_corr.index.tolist(),
        default=top_corr.index[:3].tolist()
    )

    if pairplot_features:
        fig = px.scatter_matrix(
            df,
            dimensions=pairplot_features + ["LogSalePrice"],
            color="LogSalePrice",
            title="Pairwise Relationships with LogSalePrice",
            color_continuous_scale="Viridis"
        )
        fig.update_traces(diagonal_visible=False)
        st.plotly_chart(fig)
    else:
        st.info("Select at least one feature to show pairwise relationships.")

    # --- INSIGHTS ---
    st.header("💡 Key Insights")
    st.markdown("""
- `OverallQual` and `GrLivArea` show the **strongest positive correlation** with `LogSalePrice`.
- `GarageArea`, `1stFlrSF`, and `LotArea` also contribute positively.
- Weaker correlations may add noise or multicollinearity.
- Use this analysis to focus model training on high-impact variables.
    """)

except FileNotFoundError:
    st.error("❌ Required data file not found. Please check your file paths.")

except Exception as e:
    st.error(f"⚠️ Error during correlation analysis: {e}")

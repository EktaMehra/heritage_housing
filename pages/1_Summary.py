"""
Heritage Housing – Summary Page

Purpose:
Provides a non-technical summary of the project objectives, business problem, and outcomes.
Intended for stakeholders who want a high-level understanding without code-level detail.
"""

import streamlit as st
import pandas as pd
from PIL import Image

# --- HEADER IMAGE ---
image_path = "static/images/summary_header.jpg"
output_path = "static/images/summary_header_converted.png"

try:
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img.save(output_path, format="PNG")
    st.image(output_path, use_container_width=True)
except Exception as e:
    st.warning(f"Could not load header image: {e}")

# --- PAGE TITLE ---
st.title("📌 Heritage Housing Project Summary")
st.markdown("""
This summary page gives a high-level overview of the key findings, business outcomes, and modeling results
delivered through the Heritage Housing Price Prediction App.
---
""")

# --- BUSINESS GOALS ---
st.header("📈 Business Objectives")
st.write("""
- Predict market-aligned prices for 4 inherited heritage homes
- Identify the most influential features impacting sale price
- Provide stakeholders with an interpretable, data-driven dashboard
""")

# --- EDA & MODELING TAKEAWAYS ---
st.header("📊 Key Findings from EDA & Modeling")
st.markdown("""
- **Overall Quality**, **GrLivArea**, and **GarageArea** show strong positive correlation with price
- New features like **HouseAge**, **FinishedBsmtRatio**, and **LivingLotRatio** added meaningful predictive power
- Random Forest model selected after comparing Linear Regression, XGBoost, and Gradient Boosting
- Achieved **R2 = 0.87** on test data — demonstrating strong generalization
""")

# --- VISUALS ---
st.header("🖼️ Model Performance & Inherited Property Predictions")

try:
    st.image("outputs/visuals/predicted_vs_actual_rf_vs_gbr.png", caption="Model Accuracy on Test Data")
    st.image("outputs/visuals/inherited_predictions_vs_hypothetical_actuals.png", caption="Predicted vs Expected: Inherited Properties")
except Exception as e:
    st.warning(f"Could not load performance visuals: {e}")

# --- DATA SNAPSHOT ---
st.header("📦 Processed Dataset Summary")

try:
    df = pd.read_csv("data/processed/final/X_test.csv")
    st.write(f"Rows: **{df.shape[0]}**, Columns: **{df.shape[1]}**")
    st.dataframe(df.head())

    st.subheader("📑 Feature Summary")
    st.dataframe(pd.DataFrame({
        "Data Type": df.dtypes.astype(str)
    }))
except FileNotFoundError:
    st.error("Processed dataset not found.")
except Exception as e:
    st.error(f"Error loading dataset: {e}")

# --- CONCLUSION ---
st.header("📍 Summary Takeaways")

st.markdown("""
This project delivers a practical, data-driven solution for valuing heritage homes.
The app combines statistical insights, predictive modeling, and interactive dashboards to support planning and inheritance decisions with confidence.
""")

# --- LINK TO DOCS ---
st.markdown("---")
st.info("🔍 For more technical details, visit the Technical Summary or see the README.md on GitHub.")

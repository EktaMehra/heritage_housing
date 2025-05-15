import streamlit as st
import pandas as pd
from PIL import Image

# --- Header Image ---
image_path = "static/images/summary_header.jpg"
output_path = "static/images/summary_header_converted.png"

try:
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img.save(output_path, format="PNG")
    st.image(output_path, use_container_width=True)
except Exception as e:
    st.warning(f"Could not load header image: {e}")

# --- Page Title ---
st.title("📌 Heritage Housing Project Summary")
st.markdown("""
Welcome to the summary page of the **Heritage Housing Price Prediction App**.
This project applies predictive analytics to support the valuation of inherited residential properties in Ames, Iowa.
---
""")

# --- Overview of the App ---
st.header("📋 Dashboard Navigation")
st.write("""
This app contains the following sections:
- **Home** – Project overview and navigation
- **Feature Correlation** – Explore how property features correlate with sale prices
- **Hypothesis Validation** – Validate business and modelling assumptions
- **Price Prediction** – View predictions for inherited properties and run custom ones
- **Technical Summary** – Dive into model performance and pipeline structure
""")

# --- Business Goals ---
st.header("📈 Project Goals & Business Requirements")
st.write("""
This project was developed to meet the following business needs:
- **Price Estimation**: Deliver accurate price predictions for 4 inherited houses in Ames.
- **Feature Insight**: Identify key drivers that impact sale price.
- **Decision Support**: Empower the client with a usable tool for evaluating future properties.
""")

# --- Dataset Summary ---
st.header("📦 Dataset Overview")
st.write("""
The dataset used in this project originates from [Kaggle’s Ames Housing dataset](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data).
It contains detailed information on housing attributes and final sale prices.

After preprocessing, the final dataset includes:
- Removal of outliers and missing values
- Creation of new features (e.g. `HouseAge`, `LivingLotRatio`)
- Transformation of skewed variables and log-transformation of `SalePrice`
""")

# Display Processed Dataset Info
try:
    df = pd.read_csv("data/processed/final/X_test.csv")
    st.subheader("📊 Processed Data Snapshot")
    st.write(f"Rows: **{df.shape[0]}**, Columns: **{df.shape[1]}**")
    st.dataframe(df.head())

    st.subheader("📑 Feature Summary")
    st.dataframe(pd.DataFrame({
        "Data Type": df.dtypes.astype(str)
    }))
except FileNotFoundError:
    st.error("Processed dataset not found at expected location.")
except Exception as e:
    st.error(f"Error loading dataset: {e}")

# --- More Info / README ---
st.header("🛠 Additional Information")
st.write("""
To learn more about the methodology, modelling choices, and deployment steps, refer to the full project documentation in the `README.md` file on GitHub.
""")

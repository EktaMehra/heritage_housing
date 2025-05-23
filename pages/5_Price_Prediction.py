"""
Heritage Housing – Price Prediction Page (Streamlit)

This page enables:
1. Display of predicted sale prices for inherited heritage-listed properties.
2. Custom price prediction form where users can enter property details and receive an estimated sale price.

Features:
- Form-based inputs for key structural and quality attributes
- On-the-fly feature engineering and one-hot encoding to match model training
- Real-time prediction using a serialized Random Forest pipeline
- Detailed prediction summary, user interpretation notes, and CSV download

This serves both business users (for inherited home pricing) and external users (custom scenario testing).
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image
import datetime
import os


# --- Header Image ---
image_path = "static/images/pp_header.jpg"
output_path = "static/images/pp_header_converted.png"

try:
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img = img.resize((600, 200))
        img.save(output_path, format="PNG")
    st.image(output_path, use_container_width=True)
except Exception as e:
    st.warning(f"Image load failed: {e}")

# --- Title ---
st.title("💸 Heritage Housing Price Prediction")
st.markdown("""
This page enables users to:
- View price predictions for inherited houses
- Generate sale price estimates by entering custom property attributes
---
""")

# === INHERITED PROPERTY PREDICTIONS ===
st.header("Predicted Prices for Inherited Houses")

try:
    df_inherited = pd.read_csv(
        "data/processed/final/inherited_properties_display_ready.csv")

    tabs = st.tabs([f"Property {i + 1}" for i in range(len(df_inherited))])

    for i, tab in enumerate(tabs):
        with tab:
            house = df_inherited.iloc[i].to_dict()
            price = house.pop("Predicted_SalePrice")
            house.pop("Property_ID", None)

            split = list(house.items())
            one, two, three = np.array_split(split, 3)

            st.markdown(f"""
            <div style="border: 1px solid #ccc; padding: 20px; border-radius: 10px;">
                <h3 style="color: #4CAF50;">Property {i + 1}</h3>
                <p><b>Predicted Sale Price:</b> £{price:,.2f}</p>
                <hr>
                <div style="display: flex; justify-content: space-between;">
                    {"".join([
                        f"<div style='width: 33%;'>" + "".join([
                            f"<p><b>{k}:</b> {int(v) if isinstance(v, float) and v.is_integer() else v}</p>"
                            for k, v in group]) + "</div>" for group in [one, two, three]
                        ])}
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.subheader("📜 Total Predicted Sale Value of Inherited Properties")
    st.markdown("""
    This figure represents the **combined predicted market value** of all inherited heritage properties listed above.
    The total is calculated by summing the **individual predicted sale prices** for each property.
    """)
    st.success(f"**£{df_inherited['Predicted_SalePrice'].sum():,.2f}**")

except Exception as e:
    st.error(f"❌ Could not load inherited predictions: {e}")

st.markdown("---")

# === CUSTOM PRICE PREDICTION ===
st.header("Custom Price Prediction")

with st.expander("ℹ️ How to use this form"):
    st.markdown("""
    Enter property details below to estimate the potential sale price.
    Make sure all fields are filled accurately — units are shown next to each input.
    """)

with st.form("prediction_form"):
    col1, col2, col3, col4 = st.columns(4)
    now = datetime.datetime.now().year

    with col1:
        LotFrontage = st.number_input("Lot Frontage (ft)", 0.0, 200.0, 60.0)
        MasVnrArea = st.number_input(
            "Masonry Veneer Area (sqft)", 0.0, 1500.0, 150.0)
        YearBuilt = st.number_input("Year Built", 1800, now, 1970)
        BedroomAbvGr = st.number_input("Bedrooms Above Ground", 0, 10, 3)
        GarageArea = st.number_input("Garage Area (sqft)", 0, 1500, 400)

    with col2:
        LotArea = st.number_input("Lot Area (sqft)", 1000, 30000, 8500)
        BsmtFinSF1 = st.number_input("Finished Basement (sqft)", 0, 2000, 700)
        GrLivArea = st.number_input(
            "Above Ground Living Area (sqft)", 500, 4000, 1500)
        SecondFlrSF = st.number_input("Second Floor Area (sqft)", 0, 2000, 500)
        GarageYrBlt = st.number_input("Garage Year Built", 1800, now, 1975)

    with col3:
        OpenPorchSF = st.number_input("Open Porch Area (sqft)", 0, 500, 40)
        TotalBsmtSF = st.number_input(
            "Total Basement Area (sqft)", 0, 3000, 1000)
        YearRemodAdd = st.number_input("Year Remodeled", 1800, now, 2000)
        BsmtUnfSF = st.number_input("Unfinished Basement (sqft)", 0, 2000, 300)
        FirstFlrSF = st.number_input("1st Floor Area (sqft)", 500, 2500, 1200)

    with col4:
        BsmtExposure = st.selectbox(
            "Basement Exposure", [
                "Gd", "Av", "Mn", "No"])
        BsmtFinType1 = st.selectbox(
            "Finished Basement Type", [
                "GLQ", "ALQ", "BLQ", "Rec", "LwQ", "Unf"])
        GarageFinish = st.selectbox("Garage Finish", ["Fin", "RFn", "Unf"])
        KitchenQual = st.selectbox(
            "Kitchen Quality", [
                "Ex", "Gd", "TA", "Fa", "Po"])

    OverallQual = st.slider("Overall Quality (1–10)", 1, 10, 5)
    OverallCond = st.slider("Overall Condition (1–10)", 1, 10, 5)

    submitted = st.form_submit_button("🔍 Predict Price")

if submitted:
    # --- Raw Inputs ---
    raw_input = pd.DataFrame([{
        "1stFlrSF": FirstFlrSF,
        "2ndFlrSF": SecondFlrSF,
        "BedroomAbvGr": BedroomAbvGr,
        "BsmtExposure": BsmtExposure,
        "BsmtFinSF1": BsmtFinSF1,
        "BsmtFinType1": BsmtFinType1,
        "BsmtUnfSF": BsmtUnfSF,
        "GarageArea": GarageArea,
        "GarageFinish": GarageFinish,
        "GarageYrBlt": GarageYrBlt,
        "GrLivArea": GrLivArea,
        "KitchenQual": KitchenQual,
        "LotArea": LotArea,
        "LotFrontage": LotFrontage,
        "MasVnrArea": MasVnrArea,
        "OpenPorchSF": OpenPorchSF,
        "OverallCond": OverallCond,
        "OverallQual": OverallQual,
        "TotalBsmtSF": TotalBsmtSF,
        "YearBuilt": YearBuilt,
        "YearRemodAdd": YearRemodAdd
    }])

    # --- Manual Feature Engineering ---
    raw_input["HouseAge"] = 2025 - raw_input["YearBuilt"]
    raw_input["LivingLotRatio"] = raw_input["GrLivArea"] / \
        (raw_input["LotArea"] + 1)
    raw_input["FinishedBsmtRatio"] = raw_input["BsmtFinSF1"] / \
        (raw_input["TotalBsmtSF"] + 1)
    raw_input["OverallScore"] = raw_input["OverallQual"] * \
        raw_input["OverallCond"]
    raw_input["HasPorch"] = np.where(
        raw_input["OpenPorchSF"] > 0, "Has Porch", "No Porch")

    # Drop original columns that were removed during training
    raw_input.drop(columns=[
        "YearBuilt", "GrLivArea", "LotArea", "BsmtFinSF1",
        "TotalBsmtSF", "OverallQual", "OverallCond"
    ], inplace=True)

    # --- Manual One-Hot Encoding (match training) ---
    categorical_cols = [
        "BsmtExposure",
        "BsmtFinType1",
        "GarageFinish",
        "KitchenQual",
        "HasPorch"]
    raw_input_encoded = pd.get_dummies(
        raw_input, columns=categorical_cols, drop_first=True)

    # --- Align to training features ---
    expected_cols = pd.read_csv(
        "data/processed/final/X_train.csv").columns.tolist()
    for col in expected_cols:
        if col not in raw_input_encoded.columns:
            raw_input_encoded[col] = 0
    raw_input_encoded = raw_input_encoded[expected_cols]

    # --- Load pipeline and predict ---
    try:
        pipeline = joblib.load(
            "outputs/models/final_random_forest_pipeline.pkl")
        log_prediction = pipeline.predict(raw_input_encoded)[0]
        predicted_price = np.expm1(log_prediction)

        st.success(f"💰 Predicted Sale Price: **£{predicted_price:,.2f}**")

        st.markdown("""
        📌 **Interpretation**:
        - This prediction is based on historical Ames market data and assumes similar economic conditions.
        - The model is trained to generalize well but actual sale prices may vary due to external factors (e.g. renovations, market shifts).
        - Confidence is higher for inputs that closely match the training data (e.g. typical sizes, quality ratings).
        """)

        display_df = raw_input.copy()
        display_df["Predicted SalePrice"] = predicted_price

        st.markdown("### Prediction Summary")
        st.dataframe(display_df)

        csv = display_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Prediction Data",
            data=csv,
            file_name="custom_prediction.csv",
            mime="text/csv",
        )

    except Exception as e:
        st.error(f"Prediction failed: {e}")

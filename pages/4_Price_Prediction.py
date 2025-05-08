import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image
import datetime
import os

st.set_page_config(page_title="Price Prediction", layout="wide")

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
st.header("🏠 Predicted Prices for Inherited Houses")

try:
    df_inherited = pd.read_csv("data/processed/final/inherited_properties_display_ready.csv")

    tabs = st.tabs([f"Property {i+1}" for i in range(len(df_inherited))])

    # Units dictionary
    attribute_units = {
        "LotFrontage": "ft",
        "LotArea": "sqft",
        "OpenPorchSF": "sqft",
        "MasVnrArea": "sqft",
        "BsmtFinSF1": "sqft",
        "GrLivArea": "sqft",
        "1stFlrSF": "sqft",
        "2ndFlrSF": "sqft",
        "BsmtUnfSF": "sqft",
        "GarageArea": "sqft",
        "GarageYrBlt": None,
        "YearBuilt": None,
        "YearRemodAdd": None,
        "BedroomAbvGr": "beds",
        "OverallCond": "/10",
        "OverallQual": "/10",
        "Age": "yrs",
        "LivingLotRatio": ":1",
        "FinishedBsmtRatio": None,
        "OverallScore": "/20",
        "HasPorch": None,
    }

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
                            f"<p><b>{k}:</b> {int(v) if isinstance(v, float) and v.is_integer() else v} {attribute_units.get(k, '') or ''}</p>"
                        for k, v in group]) + "</div>" for group in [one, two, three]
                    ])}
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.subheader("🧾 Total Predicted Sale Value")
    st.success(f"**£{df_inherited['Predicted_SalePrice'].sum():,.2f}**")

except Exception as e:
    st.error(f"❌ Could not load inherited predictions: {e}")

st.markdown("---")

# === CUSTOM PRICE PREDICTION ===
st.header("🎯 Custom Price Prediction")

with st.expander("ℹ️ How to use this form"):
    st.markdown("""
    Enter values for a new property below. Fields reflect those used in the model.
    Units are included where applicable.
    """)

# --- Form UI ---
raw_input_df = pd.DataFrame()
with st.form("prediction_form"):
    col1, col2, col3, col4 = st.columns(4)
    now = datetime.datetime.now().year

    with col1:
        lot_frontage = st.number_input("Lot Frontage (ft)", 0.0, 200.0, 60.0)
        mas_vnr_area = st.number_input("Masonry Veneer Area (sqft)", 0.0, 1500.0, 150.0)
        year_built = st.number_input("Year Built", 1800, now, 1970)
        bedroom_abv_gr = st.number_input("Bedrooms Above Ground", 0, 10, 3)
        garage_area = st.number_input("Garage Area (sqft)", 0, 1500, 400)

    with col2:
        lot_area = st.number_input("Lot Area (sqft)", 1000, 30000, 8500)
        bsmt_fin_sf1 = st.number_input("Finished Basement (sqft)", 0, 2000, 700)
        gr_liv_area = st.number_input("Above Ground Living Area (sqft)", 500, 4000, 1500)
        second_flr_sf = st.number_input("Second Floor Area (sqft)", 0, 2000, 500)
        garage_yr_blt = st.number_input("Garage Year Built", 1800, now, 1975)

    with col3:
        open_porch_sf = st.number_input("Open Porch Area (sqft)", 0, 500, 40)
        total_bsmt_sf = st.number_input("Total Basement Area (sqft)", 0, 3000, 1000)
        year_remod = st.number_input("Year Remodeled", 1800, now, 2000)
        bsmt_unf_sf = st.number_input("Unfinished Basement (sqft)", 0, 2000, 300)
        first_flr_sf = st.number_input("1st Floor Area (sqft)", 500, 2500, 1200)
    
    with col4:
        bsmtexposure = st.selectbox("Basement Exposure", options=["Gd", "Av", "Mn", "No"], index=1)
        bsmtfintype1 = st.selectbox("Finished Basement Type", options=["GLQ", "ALQ", "BLQ", "Rec", "LwQ", "Unf"], index=5)
        garagefinish = st.selectbox("Garage Finish Quality", options=["Fin", "RFn", "Unf"], index=2)
        kitchenqual = st.selectbox("Kitchen Quality", options=["Ex", "Gd", "TA", "Fa", "Po"], index=2)


    overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
    overall_cond = st.slider("Overall Condition (1-10)", 1, 10, 5)

    submitted = st.form_submit_button("🔍 Predict Price")

# --- Model Prediction Logic ---
if submitted:
    # Step 1: Create DataFrame from input
    input_data = pd.DataFrame([{
        "lotfrontage": lot_frontage,
        "lotarea": lot_area,
        "openporchsf": open_porch_sf,
        "masvnrarea": mas_vnr_area,
        "bsmtfinsf1": bsmt_fin_sf1,
        "totalbsmtsf": total_bsmt_sf,
        "yearbuilt": year_built,
        "grlivarea": gr_liv_area,
        "yearremodadd": year_remod,
        "overallqual": overall_qual,
        "overallcond": overall_cond,
        "bedroomabvgr": bedroom_abv_gr,
        "2ndflrsf": second_flr_sf,
        "bsmtunfsf": bsmt_unf_sf,
        "garagearea": garage_area,
        "garageyrblt": garage_yr_blt,
        "1stflrsf": first_flr_sf,
        "bsmtexposure": bsmtexposure.lower(),
        "bsmtfintype1": bsmtfintype1.lower(),
        "garagefinish": garagefinish.lower(),
        "kitchenqual": kitchenqual.lower(),
    }])


    try:
        input_data.columns = input_data.columns.str.lower()

        pipeline = joblib.load("outputs/models/final_random_forest_pipeline.pkl")
        log_prediction = pipeline.predict(input_data)[0]
        predicted_price = np.expm1(log_prediction)

        st.success(f"💰 Predicted Sale Price: **£{predicted_price:,.2f}**")

        input_data["PredictedPrice"] = predicted_price
        st.markdown("### Prediction Summary")
        st.dataframe(input_data)

        csv = input_data.to_csv(index=False).encode("utf-8")
        st.download_button(
        label="📥 Download Prediction Data",
        data=csv,
        file_name="custom_prediction.csv",
        mime="text/csv",
    )

    except Exception as e:
        st.error(f"Prediction failed: {e}")

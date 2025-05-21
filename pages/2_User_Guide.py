"""
Heritage Housing – User Guide Page

Purpose:
Offers instructions and tips to help users navigate the dashboard, interpret outputs, and use the prediction tool effectively.
"""

import streamlit as st
from PIL import Image

st.set_page_config(page_title="User Guide", layout="wide")

# --- Header Image ---
image_path = "static/images/user_guide_header.jpg"
output_path = "static/images/user_guide_banner_converted.png"

try:
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img = img.resize((600, 200))
        img.save(output_path, format="PNG")
    st.image(output_path, use_container_width=True)
except Exception as e:
    st.warning(f"Image load failed: {e}")

# --- Title ---
st.title("📘 User Guide")
st.markdown("""
This page provides instructions on how to use the Heritage Housing Price Prediction App effectively.
It is intended for clients, stakeholders, and property analysts who wish to evaluate house prices using machine learning.
---
""")

st.info("""
**Quick Start**
Use the sidebar to access prediction tools, visual insights, and model documentation.
Start with **Price Prediction** to test real or custom properties.
""")


# --- Navigation Help ---
st.header("🔍 What to Expect From Each Page")

st.markdown("""
Here’s a quick overview of what each section offers:

- 🏠 **Home**  
  Introduction to the project, client scenario, and navigation guide.

- 📚 **Summary**  
  Business context, key results, and takeaways — ideal for stakeholders.

- 📘 **User Guide**  
  You're here! Get help using the app and understanding key inputs.

- 📈 **Feature Correlation**  
  Explore how different attributes (e.g., quality, area, garage) relate to price using interactive heatmaps and scatter plots.

- ✅ **Hypothesis Validation**  
  Visual evidence for or against common assumptions (e.g., "bigger garage = higher price").

- 💸 **Price Prediction**  
  Predict sale prices for 4 inherited homes or run custom estimates.

- 📚 **Technical Summary**  
  Dive into how the model was trained, evaluated, and deployed — for technical reviewers.
""")

# --- Predict Price Section ---
st.header("🔎 Predicting House Prices")
st.subheader("Inherited Properties")
st.markdown("""
- Navigate to **Price Prediction**
- Scroll to **Predicted Prices for Inherited Houses**
- Use the tabs to view predicted prices and attributes for each house
""")

st.subheader("💸 Custom Prediction")
st.markdown("""
- Scroll to the **Custom Price Prediction** section
- Fill in the form with details like size, year built, garage info, and quality ratings
- Click **Predict Price** to generate an estimate
- The predicted sale price will appear below the form
- Optionally download the result as a CSV
""")
st.markdown("""
**What the Output Means**:
- The predicted price reflects the model's best estimate based on similar historical homes.
- Predictions are shown in GBP (£) and assume market conditions similar to those in Ames, Iowa.
- A downloadable CSV lets you retain results for reports or further use.
""")


# --- Inputs Explained ---
st.header("📥 Input Definitions")

with st.expander("Click to view input field descriptions"):
    st.markdown("""
    - **LotFrontage**: Street-connected frontage in feet
    - **LotArea**: Total lot size (sqft)
    - **1stFlrSF / 2ndFlrSF**: Finished square footage on each floor
    - **TotalBsmtSF**: Total basement area
    - **BsmtFinSF1 / BsmtUnfSF**: Finished and unfinished basement areas
    - **GarageArea / GarageYrBlt**: Garage size and construction year
    - **OpenPorchSF**: Size of open porch area
    - **YearBuilt / YearRemodAdd**: Year of construction and remodel
    - **OverallQual / OverallCond**: Overall quality and condition (rated 1–10)
    - **KitchenQual**: Kitchen quality (`Ex`, `Gd`, `TA`, `Fa`, `Po`)
    - **BsmtExposure**: Basement exposure to sunlight (`Gd`, `Av`, `Mn`, `No`)
    - **GarageFinish**: Interior finish of garage (`Fin`, `RFn`, `Unf`)
    """)

# --- Troubleshooting ---
st.header("🛠️ Troubleshooting")
st.markdown("""
- **Missing Predictions?**: Make sure all required inputs are filled. Fields like year and square footage must be non-zero.
- **Invalid Value Errors?**: Check for typos or invalid ranges (e.g., negative sqft).
- **Pipeline Errors?**: If the app shows "feature names mismatch", ensure column names and categorical values match the training data schema.

If errors persist, check the technical summary or contact the project maintainer.
""")

# --- Download / Support ---
st.header("📎 Export & Support")
st.markdown("""
- Use the **Download** buttons on most pages to export visuals and predictions
- For deployment or integration support, refer to the `README.md` and technical documentation
""")

# --- Final Note ---
st.success("This app was built as part of a predictive analytics project for Code Institute. For questions or feedback, contact the developer.")

import streamlit as st
from PIL import Image
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="Hypothesis Validation", layout="wide")

# --- HEADER IMAGE ---
image_path = "static/images/hypothesis_header.jpg"
output_path = "static/images/hypothesis_header_converted.png"

try:
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img = img.resize((500, 200))
        img.save(output_path, format="PNG")
    st.image(output_path, use_container_width=True)
except Exception as e:
    st.warning(f"Image header not loaded: {e}")

# --- PAGE TITLE ---
st.title("Hypothesis Validation")
st.markdown("""
### Evaluating Hypotheses for Heritage Housing
This section documents the business hypotheses explored in the project, the methods used to validate them, and conclusions drawn from the findings.
---
""")

# --- HYPOTHESES LIST ---
st.header("Project Hypotheses")
st.write("""
1. **Feature Impact Hypothesis**  
   - Attributes such as `OverallQual`, `GrLivArea`, and `GarageArea` are positively correlated with house sale prices.

2. **Model Performance Hypothesis**  
   - A regression model trained on the dataset can achieve **R² ≥ 0.75** on unseen test data.

3. **Inherited Properties Hypothesis**  
   - The model can predict sale prices for inherited properties aligned with market trends.
""")
st.markdown("---")

# --- HYPOTHESIS 1 ---
st.subheader(" Hypothesis 1: Feature Correlation Drives Value")
st.write("""
**Validation Steps:**
- Pearson correlation analysis
- Visual validation using scatter plots for top features
""")

def image_block(filepath, caption):
    if os.path.exists(filepath):
        st.image(filepath, caption=caption, use_container_width=True)
        with open(filepath, "rb") as file:
            st.download_button("📥 Download", data=file, file_name=os.path.basename(filepath), mime="image/png")
    else:
        st.warning(f"Missing: {filepath}")

with st.expander("📊 Pearson Correlation Heatmap"):
    image_block("outputs/visuals/pearson_correlation_heatmap.png", "Pearson Correlation Heatmap")

with st.expander("📊 GrLivArea vs LogSalePrice"):
    image_block("outputs/visuals/scatter_grlivarea_vs_LogSalePrice.png", "Living Area vs Log Sale Price")

with st.expander("📊 GarageArea vs LogSalePrice"):
    image_block("outputs/visuals/scatter_garagearea_vs_LogSalePrice.png", "Garage Area vs Log Sale Price")

st.markdown("---")

# --- HYPOTHESIS 2 ---
st.subheader("Hypothesis 2: Model Accuracy Meets Business Need")
st.write("""
**Validation Steps:**
- Trained both Random Forest and XGBoost
- Evaluated R², MAE, and RMSE on test data
""")

with st.expander("📊 R² Scores Across Models"):
    image_block("outputs/visuals/r2_scores_comparison.png", "Model R² Comparison")

with st.expander("📊 Predicted vs Actual Sale Prices"):
    image_block("outputs/visuals/predicted_vs_actual_rf_vs_gbr.png", "Predicted vs Actual on Test Data")

st.markdown("---")

# --- HYPOTHESIS 3 ---
st.subheader("Hypothesis 3: Inherited Property Pricing is Realistic")
st.write("""
**Validation Steps:**
- Predictions generated for 4 inherited houses
- Compared to market trends and analyzed residuals
""")

with st.expander("📊 Predicted vs Actual for Inherited (Log Sale Price)"):
    image_block("outputs/visuals/inherited_predictions_vs_hypothetical_actuals.png", "Predicted vs Actual (Log Scale)")

with st.expander("📊 Residuals for Random Forest Model"):
    image_block("outputs/visuals/residual_distribution_rf_inherited.png", "Residuals - Random Forest")

with st.expander("📊 Residuals for XGBoost Model"):
    image_block("outputs/visuals/residual_distribution_xgb_inherited.png", "Residuals - XGBoost")

st.markdown("---")

# --- SUMMARY & CONCLUSION ---
st.header("Hypothesis Summary")
st.write("""
- **Strong correlation** confirmed between key features and prices.
- **R² > 0.75** achieved on test data.
- **Inherited property pricing** aligned with Ames market expectations.
""")

st.header("Conclusion")
st.write("""
- Core features are strong value drivers.
- Models generalize well to unseen data.
- Inherited price predictions are reliable and explainable.

These results validate the model's business value for heritage housing scenarios.
""")

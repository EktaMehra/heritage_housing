import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Technical Summary", layout="wide")

# --- Header Image ---
image_path = "static/images/tech_summary_header.jpg"
output_path = "static/images/tech_summary_header_converted.png"

try:
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img = img.resize((500, 200))
        img.save(output_path, format="PNG")
    st.image(output_path, use_container_width=True)
except Exception as e:
    st.warning(f"Image load failed: {e}")

# --- Page Title ---
st.title("Technical Summary")
st.markdown("""
Explore the technical architecture, modelling pipeline, and performance benchmarks used to deliver sale price predictions for inherited properties in Ames, Iowa.
---
""")

# --- Pipeline Overview ---
st.header("🔧 Pipeline Design")
pipeline_section = st.radio("Select a pipeline to explore:", ["Data Cleaning", "Feature Engineering", "Model Training"])

if pipeline_section == "Data Cleaning":
    st.info("""
    The cleaning pipeline prepared the raw Kaggle dataset for modelling. It handled missing data, outliers, and inconsistencies using reproducible, rule-based steps aligned with CRISP-DM.
    """)
    st.markdown("""
    - **Missing Values**:
        - Numeric features imputed with `median` (e.g. `LotFrontage`, `GarageYrBlt`)
        - Categorical features filled with `"None"` or `"Unknown"` depending on domain logic  
    - **Outliers**:
        - Removed using IQR and 99th percentile caps  
        - Outliers in `LotArea`, `GrLivArea` and `SalePrice` were carefully reviewed
    - **Consistency**:
        - Standardized formats, renamed columns, ensured no duplicate records
    """)

elif pipeline_section == "Feature Engineering":
    st.info("""
    Feature transformations were applied to boost model learning and reduce skew. New features were introduced based on domain logic.
    """)
    st.markdown("""
    - **Created Features**:
        - `Age`, `OverallScore`, `LivingLotRatio`, `FinishedBsmtRatio`, `HasPorch`
    - **Transformations**:
        - Log-transform applied to right-skewed numerical features
        - Reflected features (`YearBuilt`, `YearRemodAdd`) for better directionality
    - **Encoding**:
        - One-hot encoding for nominal categorical features (e.g. `KitchenQual`, `BsmtExposure`)
    """)

elif pipeline_section == "Model Training":
    st.info("""
    The model pipeline integrates preprocessing and prediction in a single deployable object.
    """)
    st.markdown("""
    - **Model Selection**:
        - Compared Random Forest, XGBoost, and Gradient Boosting
        - Random Forest selected for best test R2 and lowest MAE
    - **Final Pipeline**:
        - Combined the `preprocessor` and `RandomForestRegressor` using `Pipeline()`
        - Serialized as `final_random_forest_pipeline.pkl` for use in Streamlit
    - **Cross-Validation**:
        - 5-fold CV used to validate generalization and avoid overfitting
    """)

# --- Model Performance ---
st.markdown("---")
st.header("📈 Model Performance")

st.markdown("""
Model performance was evaluated using R2, MAE, and MSE across both training and testing datasets.  
Random Forest consistently outperformed other models in both accuracy and reliability.
""")

with st.expander("📊 R2 Comparison"):
    st.image("outputs/visuals/r2_score_comparison.png", caption="R2 Score Comparison")
    with open("outputs/visuals/r2_score_comparison.png", "rb") as file:
        st.download_button("📥 Download", file, "r2_score_comparison.png", "image/png")

with st.expander("📊 Mean Absolute Error (MAE)"):
    st.image("outputs/visuals/mae_score_comparison.png", caption="MAE Comparison")
    with open("outputs/visuals/mae_score_comparison.png", "rb") as file:
        st.download_button("📥 Download", file, "mae_comparison.png", "image/png")

with st.expander("📊 Mean Squared Error (MSE)"):
    st.image("outputs/visuals/rmse_score_comparison.png", caption="MSE Comparison")
    with open("outputs/visuals/rmse_score_comparison.png", "rb") as file:
        st.download_button("📥 Download", file, "mse_comparison.png", "image/png")

# --- Feature Importance ---
st.markdown("---")
st.header("📌 Feature Importance")

st.markdown("""
The chart below shows the top 10 most important features as learned by the final Random Forest model.
These variables had the greatest influence on sale price prediction.
""")
with st.expander("📊 Top 15 Drivers"):
    st.image("outputs/visuals/rf_feature_importance_top15.png", caption="Top 15 Features by Importance")
    with open("outputs/visuals/rf_feature_importance_top15.png", "rb") as file:
        st.download_button("📥 Download", file, "top_10_features_random_forest.png", "image/png")

# --- Challenges & Improvements ---
st.markdown("---")
st.header("🚧 Challenges & Improvements")

st.markdown("""
**Challenges**:
- Data completeness: Many categorical fields had nulls requiring context-sensitive imputations
- Feature bias: Some high-cardinality fields created risk of overfitting
- Prediction pipeline complexity: Maintaining clean input schema between training and app

**Improvements**:
- Used `StandardScaler` + one-hot encoding for consistency
- Developed engineered features based on domain intuition
- Simplified pipeline deployment using `joblib` and Streamlit-ready interfaces
""")

# --- Conclusion ---
st.markdown("---")
st.header("✅ Conclusion")

st.markdown("""
The final model and pipeline met both the technical and business goals of the project:
- ✅ Achieved **R2 = 0.87** on unseen data
- ✅ Accurately predicted prices for inherited homes
- ✅ Delivered a user-friendly app for future property estimation

These results support the model’s reliability for data-driven pricing decisions in the real estate domain.
""")

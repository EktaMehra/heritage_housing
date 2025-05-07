import streamlit as st
from PIL import Image

def app():
    # === BANNER IMAGE ===
    image_path = "static/images/hypothesis_header.png"
    output_path = "static/images/hypothesis_header_converted.png"

    try:
        with Image.open(image_path) as img:
            img = img.convert("RGB")
            img = img.resize((500, 200))
            img.save(output_path, format="PNG")
    except Exception as e:
        print(f"Error processing image: {e}")
    
    st.image(output_path, use_container_width=True)

    # === PAGE TITLE ===
    st.title("🔬 Hypothesis Validation")
    st.markdown("""
    ### Evaluating Hypotheses for Heritage Housing
    This section documents the business hypotheses explored in the project, the methods used to validate them, and conclusions drawn from the findings.
    These insights support the final modelling and prediction steps for inherited properties.
    ---
    """)

    # === HYPOTHESIS LIST ===
    st.header("📋 Project Hypotheses")
    st.write("""
    The following hypotheses were formulated during the Heritage Housing analysis:

    1. **Feature Impact Hypothesis**  
       - Attributes such as `OverallQual`, `GrLivArea`, and `GarageArea` are positively correlated with house sale prices.
       - Basement finish and porch features may moderately affect prices.
    
    2. **Model Performance Hypothesis**  
       - A regression model (Random Forest or XGBoost) trained on the dataset can achieve **R² ≥ 0.75** on unseen test data.
    
    3. **Inherited Properties Hypothesis**  
       - The model can predict prices for the inherited properties within Ames’ market trend range, with acceptable residuals.
    """)
    st.markdown("---")

    # === HYPOTHESIS 1: CORRELATIONS ===
    st.subheader("🔑 Hypothesis 1: Feature Correlation Drives Value")
    st.write("""
    **Hypothesis:** Property characteristics such as quality, size, and basement finish will correlate strongly with log-transformed sale price.

    **Validation Steps:**
    - Pearson correlation analysis
    - Visual validation using scatter plots for top features
    """)

    with st.expander("📊 Pearson Correlation Heatmap"):
        st.image("outputs/visuals/pearson_correlation_heatmap.png", caption="Pearson Correlation Heatmap", use_container_width=True)
        with open("outputs/visuals/pearson_correlation_heatmap.png", "rb") as file:
            st.download_button("📥 Download Heatmap", data=file, file_name="pearson_correlation_heatmap.png", mime="image/png")

    with st.expander("📊 GrLivArea vs LogSalePrice"):
        st.image("outputs/visuals/scatter_grlivarea_vs_LogSalePrice.png", caption="Living Area vs Log Sale Price", use_container_width=True)
        with open("outputs/visuals/scatter_grlivarea_vs_LogSalePrice.png", "rb") as file:
            st.download_button("📥 Download Plot", data=file, file_name="scatter_grlivarea_vs_LogSalePrice.png", mime="image/png")

    with st.expander("📊 GarageArea vs LogSalePrice"):
        st.image("outputs/visuals/scatter_garagearea_vs_LogSalePrice.png", caption="Garage Area vs Log Sale Price", use_container_width=True)
        with open("outputs/visuals/scatter_garagearea_vs_LogSalePrice.png", "rb") as file:
            st.download_button("📥 Download Plot", data=file, file_name="scatter_garagearea_vs_LogSalePrice.png", mime="image/png")

    st.markdown("---")

    # === HYPOTHESIS 2: MODEL PERFORMANCE ===
    st.subheader("📈 Hypothesis 2: Model Accuracy Meets Business Need")
    st.write("""
    **Hypothesis:** A Random Forest or XGBoost model will achieve an R² score of at least 0.75 on the test set, indicating good generalization.

    **Validation Steps:**
    - Trained both models
    - Evaluated on test set using R², MAE, RMSE
    """)

    with st.expander("📊 R² Scores Across Models"):
        st.image("outputs/visuals/r²_score_comparison.png", caption="Model R² Comparison", use_container_width=True)
        with open("outputs/visuals/r²_score_comparison.png", "rb") as file:
            st.download_button("📥 Download", data=file, file_name="r²_score_comparison.png", mime="image/png")

    with st.expander("📊 Predicted vs Actual Sale Prices"):
        st.image("outputs/visuals/predicted_vs_actual_rf_vs_gbr.png", caption="Test Set: Predicted vs Actual", use_container_width=True)
        with open("outputs/visuals/predicted_vs_actual_rf_vs_gbr.png", "rb") as file:
            st.download_button("📥 Download", data=file, file_name="predicted_vs_actual_rf_vs_gbr.png", mime="image/png")

    st.markdown("---")

    # === HYPOTHESIS 3: INHERITED PREDICTIONS ===
    st.subheader("🏠 Hypothesis 3: Inherited Property Pricing is Realistic")
    st.write("""
    **Hypothesis:** Model-generated sale price predictions for inherited properties align with Ames' real estate market trends.

    **Validation Steps:**
    - Model applied to 4 inherited houses
    - Predictions analyzed for reasonableness and residuals
    """)

    with st.expander("📊 Predicted vs Actual for Inherited (Log Sale Price)"):
        st.image("outputs/visuals/inherited_predictions_vs_hypothetical_actuals.png", caption="Inherited Predictions (Log Scale)", use_container_width=True)
        with open("outputs/visuals/inherited_predictions_vs_hypothetical_actuals.png", "rb") as file:
            st.download_button("📥 Download", data=file, file_name="inherited_predictions_vs_hypothetical_actuals.png", mime="image/png")

    with st.expander("📊 Residuals for Random Forest Model"):
        st.image("outputs/visuals/inherited_rf_residuals.png", caption="Residuals - Random Forest", use_container_width=True)
        with open("outputs/visuals/inherited_rf_residuals.png", "rb") as file:
            st.download_button("📥 Download", data=file, file_name="inherited_rf_residuals.png", mime="image/png")

    with st.expander("📊 Residuals for XGBoost Model"):
        st.image("outputs/visuals/inherited_xgb_residuals.png", caption="Residuals - XGBoost", use_container_width=True)
        with open("outputs/visuals/inherited_xgb_residuals.png", "rb") as file:
            st.download_button("📥 Download", data=file, file_name="inherited_xgb_residuals.png", mime="image/png")

    st.markdown("---")

    # === SUMMARY ===
    st.header("🏆 Hypothesis Summary")
    st.write("""
- **Strong correlation** confirmed between features like `OverallQual`, `GrLivArea`, `GarageArea`, and sale prices.
- **Model performance** met the business requirement with **R² > 0.75**.
- **Predictions for inherited homes** were realistic and within expected range.

These findings validate the business viability of the machine learning solution for property valuation.
    """)

    st.markdown("---")

    # === CONCLUSION ===
    st.header("📊 Conclusion")
    st.write("""
The hypothesis testing confirms that:
- Core features are strong value drivers.
- The model performs reliably on unseen data.
- Inherited property pricing is defensible and explainable.

These outcomes support stakeholder decision-making and model deployment for heritage housing valuation.
    """)

"""
Heritage Housing – Home Page (Streamlit)

This is the landing page of the Heritage Housing Price Prediction App.

Purpose:
- Introduce the project and its objectives
- Explain the client scenario and inherited property context
- Outline the business requirements
- Guide users through dashboard navigation

Includes:
- Banner image
- Project overview
- Description of inherited property use case
- Business requirement summary
- Navigation guide for app sections

This page sets the foundation for users exploring price estimation and feature insights for heritage-listed residential properties.
"""

import streamlit as st
from PIL import Image

st.set_page_config(page_title="🏠 Home", layout="wide")

# --- Banner ---
image_path = "static/images/home_header.jpg"
try:
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img = img.resize((600, 200))
        st.image(img, use_container_width=True)
except Exception as e:
    st.warning(f"Banner load failed: {e}")

# --- Title and Intro ---
st.title("🏡 Heritage Housing Price Prediction App")

st.markdown("""
Welcome to the Heritage Housing Price Prediction Tool.
This app helps local councils, urban planners, and conservation officers estimate the fair market value of **heritage-listed residential properties** in Ames, Iowa.

### 🧭 Project Objective
Develop a robust machine learning model and interactive dashboard that:
- Predicts property prices with high accuracy
- Supports fair inheritance and planning decisions
- Offers explainable insights into key valuation drivers
""")

st.markdown("---")

# --- Inherited Properties Overview ---
st.header("🏘️ Client Scenario: Inherited Heritage Homes")
st.markdown("""
The client owns **4 heritage-listed properties** in Ames and wants to assess their fair market value using data-driven methods.
These properties lack sale prices and are evaluated using our trained prediction model.

📁 Input data includes:
- Lot and building dimensions
- Basement, garage, and porch features
- Construction year, renovations, and quality ratings

🧮 The model provides:
- Individual price predictions
- A combined total valuation
- Real-time forecasting via custom inputs
""")

st.markdown("---")

# --- Business Requirements ---
st.header("📌 Business Requirements")
st.markdown("""
**Requirement 1: Correlation Analysis**
- Investigate and visualize which features most strongly correlate with house sale price
- Use methods like Pearson or PPS to identify price drivers
- Summarize insights with relevant visualizations

**Requirement 2: Price Prediction System**
- Build a machine learning model that can predict the **summed price** of 4 inherited homes
- Use conventional ML (e.g., Random Forest, Gradient Boosting) with extensive hyperparameter tuning
- Ensure the system is generalizable and suitable for real-time deployment
""")

st.markdown("---")

# --- App Navigation Guide ---
st.header("🧭 Navigate the Dashboard")
st.markdown("""
Use the sidebar to explore:
- 📊 **Feature Correlation**: See which attributes impact price most
- ✅ **Hypothesis Validation**: Confirm modeling assumptions with data
- 💸 **Price Prediction**: Run estimates for inherited or custom homes
- 🧪 **Technical Summary**: Review model pipeline and performance
- 📘 **User Guide**: Understand how to use the app effectively
""")

st.markdown("---")
st.info("🔄 Built with Streamlit as part of the Code Institute PP5 Milestone Project.")

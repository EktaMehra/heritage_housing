import streamlit as st
from PIL import Image

st.set_page_config(page_title="🏠 Home", layout="wide")

# Banner image
image_path = "static/images/home_header.jpg"
try:
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img = img.resize((600, 200))
        st.image(img, use_container_width=True)
except Exception as e:
    print(f"Error loading banner: {e}")

# Title and intro
st.title("🏡 Heritage Housing Price Prediction App")
st.markdown("""
Welcome to the Heritage Housing Price Prediction Tool.
This application is designed to help local councils, urban planners, and conservation officers estimate the fair market value of heritage-listed residential properties.


Business Goals:

Enable accurate and transparent price forecasting to support:
- Fair inheritance distribution
- Urban development planning
- Property taxation and renovation funding decisions

Our machine learning model is trained on historical property data and engineered features tailored to the heritage housing market.

This app supports:
- 📊 Feature correlation analysis
- 🔬 Hypothesis validation
- 💸 Price prediction
- 📈 Model performance review
- 📁 Business & technical summaries

Use the sidebar to navigate to each section.
""")

st.markdown("---")
st.info("🔄 Built with Streamlit as part of the Code Institute PP5 Milestone Project.")

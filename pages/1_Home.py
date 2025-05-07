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
Welcome to the interactive dashboard for the **Heritage Housing Predictive Analytics** project.

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

# main.py

import streamlit as st

st.set_page_config(
    page_title="Heritage Housing Price Predictor",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Heritage Housing Price Prediction App")
st.markdown("""
Welcome to the Heritage Housing Dashboard.

Use the sidebar to explore:
- Feature correlations
- Hypothesis testing
- Price predictions
- Project insights and technical summary

---

This app is built as part of the **PP5 Predictive Analytics** milestone.
""")

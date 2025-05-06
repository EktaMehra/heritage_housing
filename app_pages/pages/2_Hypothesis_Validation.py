import numpy as np
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.load_data import load_cleaned_data
from scipy.stats import ttest_ind, f_oneway

st.title("Hypothesis Validation")
st.write("This page tests key business hypotheses using visual and statistical methods.")

df = load_cleaned_data()

# Ensure consistency
df.columns = df.columns.str.lower()

# Define updated hypotheses
hypotheses = {
    "Larger living areas increase house prices": {
        "feature": "grlivarea",
        "type": "continuous",
        "test": "correlation"
    },
    "Finished basement increases house prices": {
        "feature": "bsmtfintype1",
        "type": "binary",
        "test": "t-test",
        "value_map": {"Unf": 0, "GLQ": 1, "ALQ": 1, "BLQ": 1, "Rec": 1, "LwQ": 1, "NA": 0}
    },
    "Higher quality scores result in higher prices": {
        "feature": "overallqual",
        "type": "ordinal",
        "test": "anova"
    }
}


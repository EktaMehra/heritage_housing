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

# Select hypothesis
hypo_choice = st.selectbox("Choose a hypothesis to test", list(hypotheses.keys()))
selected = hypotheses[hypo_choice]
feature = selected["feature"]

st.markdown(f"### 🧪 Testing Hypothesis: *{hypo_choice}*")

# Log-transform target if not already
if "logsaleprice" not in df.columns:
    df["logsaleprice"] = np.log1p(df["saleprice"])

# Apply value map if needed
if selected.get("value_map"):
    df["temp_binary"] = df[feature].map(selected["value_map"])
    feature_to_use = "temp_binary"
else:
    feature_to_use = feature

# Run visual & statistical test
if selected["test"] == "correlation":
    st.write("Scatterplot vs LogSalePrice:")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[feature_to_use], y=df["logsaleprice"], ax=ax)
    st.pyplot(fig)
    corr = df[[feature_to_use, "logsaleprice"]].corr().iloc[0, 1]
    st.info(f"**Correlation**: {corr:.2f}")

elif selected["test"] == "t-test":
    st.write("Boxplot of Finished vs Unfinished Basements:")
    fig, ax = plt.subplots()
    sns.boxplot(x=df[feature_to_use], y=df["logsaleprice"], ax=ax)
    ax.set_xticklabels(["Unfinished", "Finished"])
    st.pyplot(fig)
    group1 = df[df[feature_to_use] == 1]["logsaleprice"]
    group0 = df[df[feature_to_use] == 0]["logsaleprice"]
    t_stat, p_val = ttest_ind(group1, group0, equal_var=False)
    st.info(f"**T-test p-value**: {p_val:.4f} → {'Significant' if p_val < 0.05 else 'Not significant'}")

elif selected["test"] == "anova":
    st.write("Boxplot of Overall Quality vs LogSalePrice:")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(x=df[feature_to_use], y=df["logsaleprice"], ax=ax)
    st.pyplot(fig)
    groups = [group["logsaleprice"] for _, group in df.groupby(feature_to_use)]
    f_stat, p_val = f_oneway(*groups)
    st.info(f"**ANOVA p-value**: {p_val:.4f} → {'Significant' if p_val < 0.05 else 'Not significant'}")

st.caption("Note: All hypotheses use `LogSalePrice` for stability and interpretability.")
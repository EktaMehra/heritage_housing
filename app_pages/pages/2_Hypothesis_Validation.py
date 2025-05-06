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
